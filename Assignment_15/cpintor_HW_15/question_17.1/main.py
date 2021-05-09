import sqlite3

connection = sqlite3.connect('books.db')
import pandas as pd

# 1. Select all authors' last names from the authors
# table in descending order
output_1 = pd.read_sql("""SELECT last
                            FROM authors
                            ORDER BY last DESC""",
            connection)

print('Question #1: \n', output_1)

# 2. Select all book titles from the titles table in ascending order
output_2 = pd.read_sql("""SELECT title
                    FROM titles
                    ORDER BY title ASC""", connection)

print('Question #2: \n',output_2)

# 3.
output_3 = pd.read_sql("""SELECT first, last, title, copyright, ISBN
                FROM titles
                INNER JOIN authors
                ON authors.last = 'Deitel' AND authors.first = 'Harvey'
                ORDER BY title""", connection).head()

print('Question #3: \n',output_3)

# 4. Insert a new author into the authors table
cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last)
                        VALUES ('Bill', 'Gates')""")

output_4 = pd.read_sql('SELECT * FROM authors', connection)
print('Question #4: \n',output_4)

#5.
# inserting isbn into author_ISBN table
print('\ne. ** Inserting data pertaining to new author in author_ISBN and titles tables**')
cursor.execute("""INSERT INTO author_ISBN (id, isbn)
                VALUES ('6', '1493379921')""")
print(pd.read_sql('SELECT * FROM author_ISBN ORDER BY id ASC', connection))

#inserting data into titles table
cursor.execute("""INSERT INTO titles (isbn, title, edition, copyright)
                VALUES ('1593279922', 'How to Write Your First Python Program', '1', '2020')""")
print(pd.read_sql('SELECT * FROM titles ORDER BY title ASC', connection))

print('\n\nQuestion #5: ')
print(pd.read_sql("""SELECT authors.id, titles.title, authors.last, authors.first, author_ISBN.isbn, titles.copyright
        FROM authors
        INNER JOIN author_ISBN
        ON authors.id = author_ISBN.id
        INNER JOIN titles
        ON author_ISBN.isbn = titles.isbn
        ORDER BY authors.id ASC""", connection))