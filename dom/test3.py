import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="12345678",
  database="mydatabase"
)

mycursor = mydb.cursor()

#sql = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"

#sql = "SHOW TABLES"

#sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

#sql = "DROP TABLE customers"

x = [1,2,3,4];
for a in x:
    sql = "INSERT INTO customers (name) VALUES (%s)"
    print(a)
    mycursor.execute(sql % a)


#mydb.commit()

#for x in mycursor:
#    print(x)
