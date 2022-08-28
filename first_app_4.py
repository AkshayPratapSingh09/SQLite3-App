import sqlite3

conn = sqlite3.connect("Customer.db")

c = conn.cursor()

c.execute("SELECT * FROM customers")

#Will also support slicing
# print(c.fetchone()[0]) 

#Other approach to print all the data
items = c.fetchall()

print("NAME" + "                            " + "Email")
print("______________" + "          " + "_______________________")
for item in items:
    print(item[0] + " " + item[1] + "\t\t" + item[2])
print("Command Ran Succesfully.....")

conn.commit()
conn.close()