import plotly.express as px
df = px.data.tips()
fig = px.parallel_categories(data_frame=df)
