import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("PEC2/datasets/HousingData.csv")
    df_filtered = df[['RM', 'LSTAT', 'MEDV']].dropna()
    df_filtered.rename(columns={'RM': 'Rooms', 'LSTAT': 'Lower Status', 'MEDV': 'Median Value'}, inplace=True)
    

    fig = px.scatter_matrix(
        df_filtered,
        dimensions=['Rooms', 'Lower Status', 'Median Value'],
        title=(
            "Relationship between Number of Rooms, Percentage of Lower Status Population, "
            "and Median Value of Houses in Boston"
        ),
        opacity=0.7,
        height=800,
        width=1200,
    )

    fig.update_traces(marker=dict(size=5, line=dict(width=0.5, color='DarkSlateGrey')))
    fig.update_layout(
        font=dict(size=12),
        title_font=dict(size=16),
        template='plotly_white'
    )
    
    fig.write_html("pec2-viz/matrixplot.html")

######################################################

    

    df_student = pd.read_csv("PEC2/datasets/student-mat.csv", delimiter=';')
    # Filtrar estudiantes donde G1 y G3 no sean cero
    filtered_students = df_student[(df_student['G1'] > 0) & (df_student['G3'] > 0)].dropna(subset=['G1', 'G2', 'G3'])

    # Seleccionar 2 estudiantes al azar
    random_students = filtered_students.sample(2, random_state=1)

    # Crear un objeto Figure
    fig = go.Figure()

    # Configurar la escala máxima basada en la escala de notas (0-20 convertida a 100)
    max_scale = 100

    # Añadir un indicador para cada estudiante
    for i, (index, student) in enumerate(random_students.iterrows()):
        # Normalizar las notas al rango 0-100
        G1 = (student['G1'] / 20) * 100
        G2 = (student['G2'] / 20) * 100
        G3 = (student['G3'] / 20) * 100

        # Añadir traza para cada estudiante
        fig.add_trace(go.Indicator(
            mode="number+gauge+delta", value=G3,
            delta={'reference': G1},
            domain={'x': [0.25, 1], 'y': [0.1 + i * 0.45, 0.35 + i * 0.45]},
            title={'text': f"Student {index}"},
            gauge={
                'shape': "bullet",
                'axis': {'range': [None, max_scale]},
                'threshold': {
                    'line': {'color': "red", 'width': 2},
                    'thickness': 0.75,
                    'value': G1
                },
                'steps': [
                    {'range': [0, 33], 'color': "#4d4d4d"},   # Gris oscuro
                    {'range': [33, 66], 'color': "#7f7f7f"},  # Gris intermedio
                    {'range': [66, 100], 'color': "#bfbfbf"}  # Gris claro
                ],
                'bar': {'color': "#00CC96"}
            }
        ))

    # Configurar layout del gráfico
    fig.update_layout(
        height=600,
        margin={'t': 0, 'b': 0, 'l': 0},
        paper_bgcolor='white',  # Fondo blanco
        plot_bgcolor='white',   # Fondo blanco
        showlegend=True,
        legend_title_text='Componentes',
        legend=dict(
            yanchor="top",
            y=0.95,
            xanchor="right",
            x=0.95
        )
    )

    # Añadir explicaciones en la leyenda
    fig.add_trace(go.Scatter(
        x=[None], y=[None], mode='markers',
        marker=dict(size=10, color="#00CC96"),
        legendgroup='G3', showlegend=True, name='Performance (last semester)'
    ))

    fig.add_trace(go.Scatter(
        x=[None], y=[None], mode='markers',
        marker=dict(size=10, color="red"),
        legendgroup='G1', showlegend=True, name='Performance (first semester)'
    ))

    # Eliminar ejes y grid
    fig.update_xaxes(showgrid=False, visible=False)
    fig.update_yaxes(showgrid=False, visible=False)

    # Mostrar el gráfico
    fig.show()