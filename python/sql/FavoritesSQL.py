# sqlite3 favourites.db
# .mode csv
# .import Favourties.csv favourties 
# .schema
# .timer ON

#SQLite --> BLOB, Integer, Numeric, Real, Text

import csv
from cs50 import SQL

db = SQL("sqlite:///favourites.db")

title = input("Title: ").strip()

rows = db.execute("SELECT COUNT(*) AS counter FROM favourties WHERE title LIKE ?", title)
row = rows[0]
print(row["counter"])