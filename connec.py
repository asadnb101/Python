import mysql.connector

db = mysql.connector.connect(
    host ="localhost",
    user="root",
    password= "123456",
    database="sakila"
)

query = db.cursor()
query.execute("select * from actor")
rows=query.fetchall()
query.close()
for row in rows:
    print(row)
