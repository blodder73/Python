import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="111173bl",
    database="testdb",
)

my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE testdb")

# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db[0])

# Create table
# my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")

my_cursor.execute("SHOW TABLES")

for table in my_cursor:
    print(table)

# Create records
sqlstuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"

record1 = ("John", "john@codemy.com", 40)

#my_cursor.execute(sqlstuff, record1)
#mydb.commit()

#my_cursor.execute("DELETE FROM users WHERE user_id = 3")
#mydb.commit()

my_cursor.execute("SELECT * FROM users")
for user in my_cursor:
    print(user)