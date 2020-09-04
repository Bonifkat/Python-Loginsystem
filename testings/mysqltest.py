import mysql.connector

databasemysql = mysql.connector.connect(
  host="192.168.0.102",
  user="boni",
  password="12345678",
  database="userdatabase"
)

import bcrypt

c = databasemysql.cursor()

#registration
def register():
	print("----Registeration----")

	regusername = input("Username: ")
	regpassword = input("Password: ")
	regpasswordconfirm = input("Password confirm: ")

	#Checks if password and password confirm is the same
	if regpassword == regpasswordconfirm:
		finalpw = regpasswordconfirm

		print(finalpw)
		#Password encryption
		hashedreg = bcrypt.hashpw(finalpw.encode('utf-8'), bcrypt.gensalt())

		reghashed_password = hashedreg
		
		#Database check for username
		c.execute("SELECT username FROM userdata WHERE username = %s", (regusername,))

		#global dbusername
		dbusername = 0
		for rowusername in c.fetchall():
			dbusername = rowusername[0]

		#Checks if username already exists in the database and if not create user
		if dbusername != regusername:
			#Database upload
			c.execute("INSERT INTO userdata (username, password) VALUES (%s, %s)",
				(regusername, reghashed_password))
			databasemysql.commit()

			print("------------------------")
			print("Registration Successful!")
			print("------------------------")
			menu()

		else:
			print("------------------------")
			print("Registration failed!\nUsername already has been taken.")
			print("------------------------")
			register()
	else:
		print("------------------------")
		print("Registration failed!\nPassword didn't match.")
		print("------------------------")
		register()

#login
def login():

	tryloginpasswd = b""

	print("----Login----")
	loginname = input("Username: ")
	tryloginpasswd = input("Password: ").encode('utf-8')

	#Take hashed password from user
	hashed = c.execute("SELECT password FROM userdata WHERE username = %s", (loginname,))

	#global rowpw
	rowpw = b""
	runindex = 0
	for rowpw in c.fetchall():
		loginpassword = rowpw[0]
		#str(loginpassword).encode('utf-8')
		#loginpassword.encode('utf-8')

	try:
		#check if the password is the same as the hashed one
		#if bcrypt.checkpw(tryloginpasswd, loginpassword):
		if bcrypt.checkpw(tryloginpasswd, loginpassword.encode('utf8')):
			print("------------------------")
			print("Login Successful!")
			print("------------------------")
			menu()

		else:
			print("------------------------")
			print("Login failed!\nWrong username or password.")
			print("------------------------")
			login()

	except:
		print("------------------------")
		print("Login failed!\nWrong username or password.")
		print("------------------------")
		login()

#Menu
def menu():
	menu = input("Registration(1), Login(2): ")
	#registration
	if menu == "1":
		register()
	#login
	elif menu == "2":
		login()
	#only allow the character 1 and 2
	else:
		print("You are only allowed to write 1,2 or 3.")
		menu()

menu()




"""
c = mydb.cursor()

sql = "INSERT INTO userdata (username, password) VALUES (%s, %s)"
val = ("Boni", "fkgrg&eh")
c.execute(sql, val)

mydb.commit()

print(c.rowcount, "record inserted.")
"""