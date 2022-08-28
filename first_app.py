import sqlite3


# We are using sqlite3
import sqlite3

#Connect --> will connect the file to the database
# If it doesnt exist it will create it

# conn = sqlite3.connect(":memory:")
conn = sqlite3.connect("Customer.db")

#Cursor --> It tells the database what to do
#Create Cursor
c = conn.cursor()


#Creating a table
# Two ways to write it
#1
# c.execute("CREATE TABLE customers (first_name DATATYPE,last_name DATATYPE,email DATATYPE)")

#2
c.execute("""CREATE TABLE customers (
    first_name text,
    last_name text,
    email text   
)""")

#SQLite has only 5 Datatypes ---> 
#NULL --> Doesnt Exist
#INTEGER --> Positive/Negative Numbers
#REAL --> Decimal Number
#TEXT --> String
#BLOB --> Stored as it is (mp3, image etc)

#Commit our operations
conn.commit()

#Close our connection (conn)
conn.close()

