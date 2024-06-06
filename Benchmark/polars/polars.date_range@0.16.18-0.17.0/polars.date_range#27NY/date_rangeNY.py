import polars as pl
from datetime import date
pl.date_range(closed='both', lazy=False, high=date(2022, 3, 1), low=date(2022, 1, 1))
