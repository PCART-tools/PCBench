import polars as pl
from datetime import date
pl.date_range(time_unit=None, name=None, lazy=False, low=date(2022, 1, 1), high=date(2022, 3, 1), closed='both')
