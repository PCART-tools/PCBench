import plotly.express as px
df = px.data.election()
fig = px.line_ternary(data_frame=df)
