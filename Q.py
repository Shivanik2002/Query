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

while True:
    code = int(input("Enter code:"))
    Name = input("Enter Name:")
    Salary = int(input("Enter Salary:"))
    Query = "create Table emp(code int,Name varchar(10),salary int)"
    Query1 = """insert into emp values({},'{}',{})""".format(code,Name,Salary)
    alt = """alter table emp add number int(10)"""
    update = """update emp set number = 08 where code = 128 """
    dist = """select distinct phone_no from emp """
    alt1 = """alter table emp add details varchar(20)"""
    delt = """alter table emp drop details"""


# Execute an SQL statement
    mycursor.execute(max0)


# Commit changes
    mydb.commit()
    print("data inserted successfully....")
    x = int(input("1-> Enter more/n2->Exit/nEnter choice"))
    if x == 2:
        break

show = cur.fetchone()
print(show)
# Close the connection
mydb.close()
print("connection closed!!")
 