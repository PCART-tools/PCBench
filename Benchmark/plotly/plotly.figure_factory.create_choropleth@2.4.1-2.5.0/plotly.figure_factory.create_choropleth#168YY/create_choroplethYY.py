import plotly.plotly as py
import plotly.figure_factory as ff
import numpy as np
import pandas as pd
df_sample = pd.read_csv('minoritymajority.csv')
df_sample_r = df_sample[df_sample['STNAME'] == 'Florida']
values = df_sample_r['TOT_POP'].tolist()
fips = df_sample_r['FIPS'].tolist()
binning_endpoints = list(np.mgrid[min(values):max(values):4j])
colorscale = ['#030512', '#1d1d3b', '#323268', '#3d4b94', '#3e6ab0', '#4989bc', '#60a7c7', '#85c5d3', '#b7e0e4', '#eafcfd']
fig = ff.create_choropleth(fips=fips, values=values, scope=['Florida'], binning_endpoints=binning_endpoints, colorscale=colorscale, order=None, simplify_county=0.02, simplify_state=0.02, asp=None, offline_mode=False, show_hover=True, show_state_data=True, state_outline=None, county_outline=None, centroid_marker=None, round_legend_values=True, exponent_format=True)
