import polars as pl
from datetime import date
pl.date_range(closed='both', low=date(2022, 1, 1), interval='1mo', high=date(2022, 3, 1))
