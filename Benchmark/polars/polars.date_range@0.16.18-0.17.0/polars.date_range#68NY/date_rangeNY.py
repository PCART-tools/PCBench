import polars as pl
from datetime import date
pl.date_range(high=date(2022, 3, 1), name=None, interval='1mo', closed='both', lazy=False, low=date(2022, 1, 1))
