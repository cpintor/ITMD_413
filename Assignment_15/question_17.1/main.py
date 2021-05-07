import sqlite3

connection = sqlite3.connect('books.db')
import pandas as pd

# 1. Select all authors' last names from the authors
# table in descending order
output_1 = pd.read_sql("""SELECT last
                            FROM authors
                            ORDER BY last DESC""",
            connection)

print(output_1)

# 2. Select all book titles from the titles table in ascending order
output_2 = pd.read_sql("""SELECT title
                    FROM titles
                    ORDER BY title""", connection)

print(output_2)

