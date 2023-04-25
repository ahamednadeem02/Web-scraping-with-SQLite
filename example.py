import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)

'''new_row = [('a', 'b', 'c'),
           ('d', 'e', 'f')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_row)
connection.commit()'''