import sqlite3

connection = sqlite3.connect("C:\itstep.sl3", 5)
cur = connection.cursor()
# cur.execute("INSERT INTO first_table (name) VALUES ('Ann');")
# cur.execute("INSERT INTO first_table (name) VALUES ('Kats');")
# cur.execute("INSERT INTO first_table (name) VALUES ('John');")
cur.execute("SELECT rowid, name FROM first_table WHERE rowid = 4 ")
connection.commit()
# cur.execute("CREATE TABLE first_table (name TEXT);")
# cur.execute("INSERT INTO first_table (name) VALUES ('Nick');")
# cur.execute("SELECT rowid, name FROM first_table;")

res = cur.fetchall()
print(res)
connection.close()
