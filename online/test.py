import sqlite3

conn1 = sqlite3.connect('db.sqlite3')
c = conn1.cursor()
c.execute(f"SELECT * FROM  sqlite_master WHERE   type='table'")
Clients_info = c.fetchall()

conn1.commit()
conn1.close()  

print(Clients_info)