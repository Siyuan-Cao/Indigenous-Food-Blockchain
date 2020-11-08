import sqlite3

con = sqlite3.connect('foodsystem.db')
con.execute("drop table if exists admin")
con.execute("drop table if exists employee")
con.execute("drop table if exists ledger")
con.execute("drop table if exists harvester")
con.execute("drop table if exists manufacturer")
con.execute("drop table if exists seller")
con.execute("drop table if exists product")

print("Database Opened successfully")

con.execute("create table Employee (id INTEGER PRIMARY KEY AUTOINCREMENT , name TEXT NOT NULL, password TEXT NOT NULL, type VARCHAR(1) NOT NULL)")
con.execute("create table Product (id INTEGER PRIMARY KEY AUTOINCREMENT , product TEXT NOT NULL, img_filename TEXT, product_info TEXT NOT NULL)")
con.execute("create table Harvester (id INTEGER PRIMARY KEY AUTOINCREMENT, harvester TEXT NOT NULL, harvester_info TEXT NOT NULL, harvest_time TEXT NOT NULL, harvest_location TEXT NOT NULL, harvest_batch TEXT NOT NULL)")
con.execute("create table Manufacturer (id INTEGER PRIMARY KEY AUTOINCREMENT, manufacturer TEXT NOT NULL, manufacturer_info TEXT NOT NULL)")
con.execute("create table Seller (id INTEGER PRIMARY KEY AUTOINCREMENT, seller TEXT NOT NULL, seller_info TEXT NOT NULL)")

con.execute("create table Ledger (id INTEGER PRIMARY KEY AUTOINCREMENT, product_id INTEGER, harvester_id INTEGER, manufacturer_id INTEGER, seller_id INTEGER, FOREIGN KEY (product_id) REFERENCES product(id), FOREIGN KEY (harvester_id) REFERENCES harvester(id), FOREIGN KEY (manufacturer_id) REFERENCES manufacturer(id), FOREIGN KEY (seller_id) REFERENCES seller(id))")
cur=con.cursor()

name="admin"
password="admin"
emp_type="a"

name1="e1"
password1="e1"
emp_type1="e"

name2="h1"
password2="h1"
emp_type2="h"

name3="m1"
password3="m1"
emp_type3="m"

name4="s1"
password4="s1"
emp_type4="s"

cur.execute("INSERT into employee (name,password,type)values (?, ?, ?)", (name, password, emp_type))
cur.execute("INSERT into employee (name,password,type)values (?, ?, ?)", (name1, password1, emp_type1))
cur.execute("INSERT into employee (name,password,type)values (?, ?, ?)", (name2, password2, emp_type2))
cur.execute("INSERT into employee (name,password,type)values (?, ?, ?)", (name3, password3, emp_type3))
cur.execute("INSERT into employee (name,password,type)values (?, ?, ?)", (name4, password4, emp_type4))

con.commit()
with con:
	cur=con.cursor()
	cur.execute("SELECT * FROM employee")
	rows =cur.fetchall()

	print(rows)
	for row in rows:
		print(row)

print ("Table created successfully")