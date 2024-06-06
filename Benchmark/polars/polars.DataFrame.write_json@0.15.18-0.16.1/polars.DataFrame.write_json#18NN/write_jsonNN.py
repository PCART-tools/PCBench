import polars as pl
df = pl.DataFrame({'A': [1, 2, 3, 4, 5], 'B': ['a', 'b', 'c', 'd', 'e']})
df.write_json('output.json', row_oriented=False, to_string=None, pretty=False)
