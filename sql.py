import pymysql

# Connect to MySQL
mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="Tawny@123",
  database="test"
)

# Create a cursor object
mycursor = mydb.cursor()

query1 = "CREATE TABLE new_table (name VARCHAR(255), address VARCHAR(255))"
query2 = """insert into new_table values ("Antim","ujjain")"""

query3 = "create table student_1(id int, name varchar(12),class varchar(10),Address varchar(15))"
query4 = """insert into student_1 values (111,"muskan","12th","Ujjain"),(112,"Anika","first_year","Indore")"""
list1 = [query2,query4]

for i in list1:
# Execute an SQL statement
  mycursor.execute(i)
  print("query execute:",i)

# Commit changes
mydb.commit()

# Close the connection
mydb.close()
 

