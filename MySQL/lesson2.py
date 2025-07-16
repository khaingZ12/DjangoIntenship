import sqlite3

con = sqlite3.connect('mynote.db')
cur = con.cursor()

get_id = int(input('Enter ID Number : '))
get_name = input('Enter Name : ')
get_status = input('Enter Status : ')

def insertdata(get_id, get_name, get_status):
    cur.execute("insert into dailytask values(?,?,?)", (get_id, get_name, get_status))

def update_data():
    cur.execute("update dailytask set name =? where id =?", (get_name,get_id))

def delete_data():
    cur.execute("delete from dailytask where id=?",(get_id,))

# insertdata(get_id, get_name, get_status)
# update_data()
delete_data()


con.commit()
con.close()
