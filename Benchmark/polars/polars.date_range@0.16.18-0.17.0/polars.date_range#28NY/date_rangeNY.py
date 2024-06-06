import polars as pl
from datetime import date
pl.date_range(low=date(2022, 1, 1), lazy=False, closed='both', name=None, high=date(2022, 3, 1))
