import sqlite3
 
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
create_table = "CREATE TABLE IF NOT EXISTS users (id int, username text, password text)" ## create schema
cursor.execute(create_table)

user = (1, 'dodo', 'root')
insert_user = "INSERT INTO  users values (?,?,?)" ## insert data
cursor.execute(insert_user, user)

users = [
    (2, 'dodo2', 'root2'),
    (3, 'dodo3', 'root3'), 
]

cursor.executemany(insert_user, users) ## insert multiple data

select_query =  "SELECT * FROM users" ## select data
results = cursor.execute(select_query)
for row in results:
    print(row)

connection.commit() ## flush data on file
connection.close()  ## close connection to db

