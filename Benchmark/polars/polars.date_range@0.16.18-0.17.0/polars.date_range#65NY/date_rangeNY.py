import polars as pl
from datetime import date
pl.date_range(time_unit=None, interval='1mo', low=date(2022, 1, 1), high=date(2022, 3, 1))
