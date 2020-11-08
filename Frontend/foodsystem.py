from flask import *  
import sqlite3
import hashlib
import pyqrcode
import png
  
app = Flask(__name__)  
@app.route("/")  
def index():  
    return render_template("homepage.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/team")
def team():
	return render_template("team.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")

@app.route("/login")  
def login():  
    return render_template("login.html")

@app.route("/userLogin", methods=['POST','GET'])
def adminLogin():
	error=""
	if request.method=='POST':
		
		admin = request.form['username']
		password = request.form['password']
		usertype = request.form['dropdown']
		if usertype=="Admin":
			validate = valid(admin, password)
			if validate == False:
				error = 'Invalid Credentials'
			else:
				return redirect(url_for('admin'))
		else:
			validate = validEmployee(admin, password, usertype)
			if validate == False:
				error = 'Invalid Credentials'
			else:
				return render_template("employeepage.html", user=usertype)

	return render_template('login.html',error=error)

def valid(admin, password):
	con=sqlite3.connect('foodsystem.db')
	validate=False
	with con:
		cur=con.cursor()
		cur.execute("Select * FROM employee")
		rows =cur.fetchall()
		for row in rows:
			dbAdmin = row[1]
			dbPass  = row[2]
			dbuser  = row[3]
			if dbuser == "a":
				if dbAdmin == admin:
					print("Matched")
					if dbPass == password:
						validate= True
	return validate

def validEmployee(admin, password, usertype):
	con=sqlite3.connect('foodsystem.db')
	validate=False
	with con:
		cur=con.cursor()
		cur.execute("Select * FROM employee")
		rows =cur.fetchall()
		for row in rows:
			dbAdmin = row[1]
			dbPass  = row[2]
			dbType  = row[3]
			
			if dbType == usertype[0].lower():
				if dbAdmin == admin:
					print("Matched")
					if dbPass == password:
						validate= True
	return validate

@app.route("/adminpage")
def admin():
	return render_template("adminpage.html")

@app.route("/employee/<string:user>")
def employee(user):
	return render_template("employeepage.html", user=user)

@app.route("/adduser")
def addemployee():
	return render_template("adduser.html")

@app.route("/saveuser", methods=["POST","GET"])
def saveDetails():
	message = "Nothing"
	if request.method == "POST":
		try:
			username = request.form["username"]
			password = request.form["password"]
			usertype = request.form["usertype"]
			with sqlite3.connect("foodsystem.db") as con:
				cur = con.cursor()
				cur.execute ("INSERT into employee (name,password,type)values (?, ?, ?)", (username, password, usertype))
				con.commit()
				message = "User added Successfully"
				print(message)
		except:
			con.rollback()
			message = "Not able to add user"
		finally:
			con.close()
			return render_template("adminpage.html", message=message)

@app.route("/deleteuser")
def deleteemployee():
	con=sqlite3.connect('foodsystem.db')
	cur = con.cursor()
	cur.execute("select id, name from employee")
	rows=cur.fetchall()
	return render_template("deleteuser.html", rows=rows)

@app.route("/removeuser", methods=["POST","GET"])
def deleteRecord1():
	id=request.form["user"]
	with sqlite3.connect("foodsystem.db") as con:
		try:
			cur = con.cursor()
			cur.execute ("delete from employee where id = ?", (id))
			con.commit()
			message = "User Deleted Successfully"
		except:
			message ="User cannot be deleted"
		finally:
			return render_template("adminpage.html", message=message)


@app.route("/qrgenerate/<string:user>")
def qrgenerate(user):
	return render_template("qrgenerate.html", user=user)

@app.route("/converted/<string:user>", methods=['POST'])
def qrGenerated(user):
	product = request.form['name']
	qrGen(product)
	filename = 'qr.png'
	return send_file(filename,as_attachment=True, user=user)

def qrGen(s):
    qr = pyqrcode.create(s)
    qr.png('qr.png',scale = 8)

@app.route("/addproduct/<string:user>,<string:addtype>", methods=['POST','GET'])
def addProduct(user,addtype):
	con=sqlite3.connect('foodsystem.db')
	cur = con.cursor()
	if request.method == "POST":
		skip = request.form['skip']
		if skip == "h":
			cur.execute("insert into Ledger(product_id) select max(id) from product")
			con.commit()
		elif skip == "m":
			if addtype == "h":
				product = request.form['product']
				cur.execute("insert into Ledger(product_id) values(?)", (product))
				con.commit()
				cur.execute("update Ledger set harvester_id=(select max(h.id) from harvester h) where id=(select max(l.id) from ledger l)")
			else:
				cur.execute("insert into Ledger(product_id, harvester_id) select max(p.id), max(h.id) from product p, harvester h")
			con.commit()
		elif skip == "s":
			if addtype == "h":
				product = request.form['product']
				cur.execute("insert into Ledger(product_id) values(?)", (product))
				con.commit()
				cur.execute("update Ledger set harvester_id=(select max(h.id) from harvester h) where id=(select max(l.id) from ledger l)")
				con.commit()
				cur.execute("update Ledger set manufacturer_id=(select max(m.id) from manufacturer m) where id=(select max(l.id) from ledger l)")
			elif addtype == "m":
				product = request.form['product']
				harvester = request.form['harvester']
				cur.execute("insert into Ledger(product_id, harvester_id) values(?,?)", (product,harvester))
				con.commit()
				cur.execute("update Ledger set manufacturer_id=(select max(m.id) from manufacturer m) where id=(select max(l.id) from ledger l)")
			else:
				cur.execute("insert into Ledger(product_id, harvester_id, manufacturer_id) select max(p.id), max(h.id), max(m.id) from product p, harvester h, manufacturer m")
			con.commit()
		con.close()
		return render_template("employeepage.html", user=user, message="p", newMessage="Added Successfully")
	else:
		if addtype=="h":
			cur.execute("select * from product")
			rows=cur.fetchall()
			return render_template("addharvester.html", message="h", user=user, addtype=addtype, rows=rows)
		if addtype=="m":
			cur.execute("select * from product")
			rows=cur.fetchall()
			cur.execute("select * from harvester")
			rows1=cur.fetchall()
			return render_template("addmanufacturer.html", message="m", user=user, addtype=addtype, rows=rows, rows1=rows1)
		if addtype=="s":
			cur.execute("select * from product")
			rows=cur.fetchall()
			cur.execute("select * from harvester")
			rows1=cur.fetchall()
			cur.execute("select * from manufacturer")
			rows2=cur.fetchall()
			return render_template("addseller.html", message="s", user=user, addtype=addtype, rows=rows, rows1=rows1, rows2=rows2)
		return render_template("addproduct.html", user=user, message="p")

@app.route("/saveproduct/<string:user>", methods=['POST'])
def saveProduct(user):
	con=sqlite3.connect('foodsystem.db')
	try:
		product = request.form['product']
		img_filename = request.form['img_filename']
		product_info = request.form['product_info']
		cur = con.cursor()
		cur.execute ("INSERT into product (product, img_filename, product_info) values(?,?,?)", (product, img_filename, product_info))
		con.commit()
		# cur.execute("insert into Ledger(product_id) select max(id) from product")
		# print("added to ledger")
		# con.commit()
		# cur.execute("select * from ledger")
		# rows = cur.fetchall()
		# print(rows)
		product
		message="h"
	except:
		con.rollback()
		message = "Not able to add product"
	finally:
		con.close()
		return render_template("addproduct.html", message=message, user=user)

@app.route("/addharvester/<string:user>,<string:addtype>", methods=['POST'])
def addharvester(user,addtype):
	con=sqlite3.connect('foodsystem.db')
	try:
		if addtype == "h":
			product = request.form['product']
		harvester = request.form['harvester']
		harvester_info = request.form['harvester_info']
		harvest_time = request.form['harvest_time']
		harvest_location = request.form['harvest_location']
		harvest_batch = request.form['harvest_batch']
		cur = con.cursor()
		cur.execute ("INSERT into harvester (harvester, harvester_info, harvest_time, harvest_location, harvest_batch) values(?,?,?,?,?)", (harvester, harvester_info, harvest_time, harvest_location, harvest_batch))
		con.commit()
		message="m"
	except:
		con.rollback()
		message = "Not able to add product"
	finally:
		con.close()
		if addtype=="h":
			return render_template("addharvester.html", message=message, user=user, addtype=addtype, product=product)
		return render_template("addproduct.html", message=message, user=user)

@app.route("/addmanufacturer/<string:user>,<string:addtype>", methods=['POST'])
def addmanufacturer(user,addtype):
	con=sqlite3.connect('foodsystem.db')
	try:
		if addtype == "h":
			product = request.form['product']
		if addtype == "m":
			product = request.form['product']
			harvester = request.form['harvester']
		manufacturer = request.form['manufacturer']
		manufacturer_info = request.form['manufacturer_info']
		cur = con.cursor()
		cur.execute ("INSERT into manufacturer (manufacturer, manufacturer_info) values(?,?)", (manufacturer, manufacturer_info))
		con.commit()
		message="s"
	except:
		con.rollback()
		message = "Not able to add product"
	finally:
		con.close()
		if addtype=="h":
			return render_template("addharvester.html", message=message, user=user, addtype=addtype, product=product)
		if addtype=="m":
			return render_template("addmanufacturer.html", message=message, user=user, addtype=addtype, product=product, harvester=harvester)
		return render_template("addproduct.html", message=message, user=user)

@app.route("/addseller/<string:user>,<string:addtype>", methods=['POST'])
def addseller(user,addtype):
	con=sqlite3.connect('foodsystem.db')
	try:
		if addtype == "h":
			product = request.form['product']
		if addtype == "m":
			product = request.form['product']
			harvester = request.form['harvester']
		if addtype == "s":
			product = request.form['product']
			harvester = request.form['harvester']
			manufacturer = request.form['manufacturer']
		seller = request.form['seller']
		seller_info = request.form['seller_info']
		cur = con.cursor()
		cur.execute ("INSERT into seller (seller, seller_info) values(?,?)", (seller, seller_info))
		con.commit()
		if addtype=="s":
			cur.execute("insert into Ledger(product_id, harvester_id, manufacturer_id) values(?,?,?)", (product,harvester,manufacturer))
			con.commit()
			cur.execute("update Ledger set seller_id=(select max(s.id) from seller s) where id=(select max(l.id) from ledger l)")
		else:
			cur.execute("insert into Ledger(product_id, harvester_id, manufacturer_id, seller_id) select max(p.id), max(h.id), max(m.id), max(s.id) from product p, harvester h, manufacturer m, seller s")
		con.commit()
		newMessage="Added Successfully"
	except:
		con.rollback()
		newMessage = "Not able to add product"
	finally:
		con.close()
		return render_template("employeepage.html", user=user, newMessage=newMessage)

@app.route("/viewyourproducts/<string:user>")
def viewyourproducts(user):
	con=sqlite3.connect('foodsystem.db')
	cur = con.cursor()
	rows=cur.fetchall()
	return render_template("yourproducts", rows=rows, user=user)

@app.route("/downloadqr/<string:id>")
def downloadqr(id):
	qrtext = "http://127.0.0.1:5000/displayproduct/" + id
	qr = pyqrcode.create(qrtext)
	qr.png(id+'.png',scale = 8)
	filename = id+'.png'
	return send_file(filename,as_attachment=True)

@app.route("/viewproducts/<string:user>")
def viewProducts(user):
	con=sqlite3.connect('foodsystem.db')
	cur = con.cursor()
	cur.execute("select l.id, p.product, h.harvester, m.manufacturer, s.seller from ledger l left join product p on p.id=l.product_id left join harvester h on h.id=l.harvester_id left join manufacturer m on m.id=l.manufacturer_id left join seller s on s.id=l.seller_id")
	rows=cur.fetchall()
	return render_template("viewallproducts.html", rows=rows, user=user)

@app.route("/viewallproducts")
def viewAllProducts():
	con=sqlite3.connect('foodsystem.db')
	cur = con.cursor()
	cur.execute("select l.id, p.product, p.img_filename, h.harvester, m.manufacturer, s.seller from ledger l left join product p on p.id=l.product_id left join harvester h on h.id=l.harvester_id left join manufacturer m on m.id=l.manufacturer_id left join seller s on s.id=l.seller_id")
	rows=cur.fetchall()
	return render_template("viewproduct.html", rows=rows)

@app.route("/displayproduct/<string:id>")
def displayproduct(id):
	con=sqlite3.connect('foodsystem.db')
	cur = con.cursor()
	cur.execute("select l.id, p.product, p.img_filename, p.product_info, h.harvester, h.harvester_info, h.harvest_time, h.harvest_location, h.harvest_batch, m.manufacturer, m.manufacturer_info, s.seller, s.seller_info from ledger l left join product p on p.id=l.product_id left join harvester h on h.id=l.harvester_id left join manufacturer m on m.id=l.manufacturer_id left join seller s on s.id=l.seller_id where l.id=?", [id])
	rows=cur.fetchall()
	return render_template("displayproduct.html", rows=rows)

if __name__ == "__main__":  
    app.run(debug = True) 