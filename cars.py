# Working with SQL Tables

import sqlite3
 
# connect to the database 
connection = sqlite3.connect("cars.db")
 
# cursor 
con = connection.cursor()

# Code Commented Out after database was created and added to
 
### create a table
##createInv = """CREATE TABLE inventory ( 
##    id INTEGER PRIMARY KEY, 
##    brand STRING, 
##    model STRING, 
##    milage INTEGER, 
##    price INTEGER);"""
 
# execute the statement
# con.execute(createInv)
 
### insert car data
##addInv = """INSERT INTO inventory VALUES (1, "Honda", "Accord", 2123, 23000);"""
##con.execute(addInv)
## 
### another car
##addInv = """INSERT INTO inventory VALUES (2, "Toyota", "Camry", 34, "27000");"""
##con.execute(addInv)

 
con.execute("SELECT * FROM inventory") 
 
stock = con.fetchall() 
 
for i in stock:
    print(i)

##(1, 'Honda', 'Accord', 2123, 23000)
##(2, 'Toyota', 'Camry', 34, 27000)
##>>> 

connection.commit()

connection.close()

