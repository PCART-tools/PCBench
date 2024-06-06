import polars as pl
from datetime import date
pl.date_range(high=date(2022, 3, 1), name=None, low=date(2022, 1, 1), lazy=False, interval='1mo', time_unit=None, closed='both')
