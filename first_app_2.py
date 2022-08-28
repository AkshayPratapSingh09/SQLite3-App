
# We are using sqlite3
import sqlite3

#Connect --> will connect the file to the database
# If it doesnt exist it will create it

# conn = sqlite3.connect(":memory:")
conn = sqlite3.connect("Customer.db")

#Cursor --> It tells the database what to do
#Create Cursor
c = conn.cursor()

#-----------To add Single data at a time ---------------
c.execute("INSERT INTO customers VALUES ('Watson','Pal','golughat@gmail.com')")

print("Data Added Successfully.....")


#-----------To add multiple data at a time -------------
many_customers = [('Billy', 'Eilish','joblessmuse@gmail.com'),
                    ('Faltu', 'Launda', 'dude@gmail.com')
                    ]

c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)

print("Data Added Successfully.....")

conn.commit()
conn.close()