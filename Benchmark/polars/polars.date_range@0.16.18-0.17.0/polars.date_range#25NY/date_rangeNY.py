import polars as pl
from datetime import date
pl.date_range(low=date(2022, 1, 1), time_unit=None, high=date(2022, 3, 1))
