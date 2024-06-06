import plotly.express as px
df = px.data.gapminder()
fig = px.area(df,  'year',  'pop', line_group='country')
