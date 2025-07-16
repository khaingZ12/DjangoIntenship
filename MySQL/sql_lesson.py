import mysql.connector

cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root"
)
print(cnx)
# open
cur = cnx.cursor()

cur.execute("create database pdata")

# save
cnx.commit()
cnx.close()