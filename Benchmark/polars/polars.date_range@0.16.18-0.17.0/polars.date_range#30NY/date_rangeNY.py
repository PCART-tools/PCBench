import polars as pl
from datetime import date
pl.date_range(low=date(2022, 1, 1), high=date(2022, 3, 1), time_zone=None, closed='both', lazy=False, name=None, time_unit=None)
