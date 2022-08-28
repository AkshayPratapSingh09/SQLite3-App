
# We are using sqlite3
import sqlite3

#Connect --> will connect the file to the database
# If it doesnt exist it will create it

# conn = sqlite3.connect(":memory:")
conn = sqlite3.connect("Customer.db")

#Cursor --> It tells the database what to do
#Create Cursor
c = conn.cursor()

#Used query to display the result
c.execute("SELECT * FROM customers")

#Other formats to get the data
#c.fetchone() --> fetch data by index
print(c.fetchmany(2)) #--> Fetch data by amount of numbers
#c.fetchall() --> fetch all data

print("Command Ran Succesfully.....")

conn.commit()
conn.close()