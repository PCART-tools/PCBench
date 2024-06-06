import polars as pl
from datetime import date
pl.date_range(interval='1mo', lazy=False, low=date(2022, 1, 1), high=date(2022, 3, 1))
