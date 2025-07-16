import sqlite3

con = sqlite3.connect("mynote.db")

cur = con.cursor()
# create table
cur.execute("create table if not exists dailytask(id int, name varchar(50), status varchar(50))")

get_id = int(input('Enter ID Number : '))
get_name = input('Enter Name : ')
get_status = input('Enter Status : ')

cur.execute("insert into dailytask values(?,?,?)", (get_id, get_name, get_status))


con.commit()
con.close()
