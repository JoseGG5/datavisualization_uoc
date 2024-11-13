import plotly.express as px
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("PEC2/datasets/HousingData.csv")
    df_filtered = df[['RM', 'LSTAT', 'MEDV']].dropna()
    fig = px.scatter_matrix(df_filtered, dimensions=['RM', 'LSTAT', 'MEDV'], title="Pair Plot de RM, LSTAT y MEDV")
    fig.show()

