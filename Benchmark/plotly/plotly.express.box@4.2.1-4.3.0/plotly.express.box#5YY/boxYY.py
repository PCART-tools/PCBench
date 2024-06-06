import plotly.express as px
df = px.data.tips()
fig = px.box(df, x='time')
