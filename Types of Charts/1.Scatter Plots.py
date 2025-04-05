

# x and y given as array_like objects
import plotly.express as px
fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
fig.show()






df = px.data.iris() # iris is a pandas DataFrame
fig_1 = px.scatter(df, x="sepal_width", y="sepal_length")
fig_1.show()






fig_2 = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
fig_2.show()





