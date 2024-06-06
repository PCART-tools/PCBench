import polars as pl
country_code_dict = {'CA': 'Canada', 'DE': 'Germany', 'FR': 'France', None: 'Not specified'}
df = pl.DataFrame({'country_code': ['FR', None, 'ES', 'DE']}).with_row_count()
df.with_columns(pl.col('country_code').map_dict(remapping=country_code_dict, default=None, dtype=None).alias('remapped'))
