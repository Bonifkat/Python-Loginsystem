import bcrypt
import sqlite3

#name of the database file (userdatabase.db)
conn = sqlite3.connect('userdatabase.db')
c = conn.cursor()

#Creates SQLite file if missing.
c.execute('CREATE TABLE IF NOT EXISTS userdata(username REAL, password REAL)')

#registration
def register():

	#Visual stuff
	print("----Registeration----")

	username_register_input = input("Username: ")
	password_register_input = input("Password: ")
	password_register_confirm_input = input("Password confirm: ")

	#Check if username has only alphanumeric characters
	if username_register_input.isalnum() == True:

		#Check if username has only alphanumeric characters
		if password_register_input.isalnum() == True:

			#Checks if password and password confirm is the same
			if password_register_input == password_register_confirm_input:
				password_to_hash = password_register_confirm_input

				#Password encryption
				encrypt_password = bcrypt.hashpw(password_to_hash.encode('utf-8'), bcrypt.gensalt())

				hashed_registered_password = encrypt_password
				
				#Database check for username
				c.execute("SELECT username FROM userdata WHERE username = ?", (username_register_input,))

				usernames_from_db = 0
				for checkusername in c.fetchall():
					usernames_from_db = checkusername[0]

				#Checks if username already exists in the database and if not create user.
				if usernames_from_db != username_register_input:
					#Database upload
					c.execute("INSERT INTO userdata (username, password) VALUES (?, ?)",
						(username_register_input, hashed_registered_password))
					conn.commit()

					#Visual stuff
					print("------------------------")
					print("Registration Successful!")
					print("------------------------")
					menu()

				else:
					#Visual stuff
					print("------------------------")
					print("Registration failed!\nUsername already has been taken.")
					print("------------------------")
					register()
			else:
				#Visual stuff
				print("------------------------")
				print("Registration failed!\nPassword didn't match.")
				print("------------------------")
				register()

		else:
			#Visual stuff
			print("------------------------")
			print("Registration failed!\nYou can only use alphanumeric characters.")
			print("------------------------")
			register()

			
	else:
		#Visual stuff
		print("------------------------")
		print("Registration failed!\nYou can only use alphanumeric characters.")
		print("------------------------")
		register()

#login
def login():

	password_login_input = b""

	print("----Login----")
	loginname_login_input = input("Username: ")
	password_login_input = input("Password: ").encode('utf-8')

	#Take hashed password from user
	gethashed = c.execute("SELECT password FROM userdata WHERE username = ?", (loginname_login_input,))

	password_import_from_db = b""
	for password_import_from_db in c.fetchall():
		password_from_db = password_import_from_db[0]
		str(password_from_db).encode('utf-8')

	try:
		#check if the password is the same as the hashed one
		if bcrypt.checkpw(password_login_input, password_from_db):
			#Login Success.
			print("------------------------")
			print("Login Successful!")
			print("------------------------")
			menu()

		else:
			#Error for wrong password.
			print("------------------------")
			print("Login failed!\nWrong username or password.")
			print("------------------------")
			login()

	except:
		#Error for wrong username.
		print("------------------------")
		print("Login failed!\nWrong username or password.")
		print("------------------------")
		login()

#Menu
def menu():

	menu = input("Registration(1), Login(2): ")

	#Registration menu
	if menu == "1":
		register()

	#Login menu
	elif menu == "2":
		login()

	#Error for pressing anything else than the key 1 and 2.
	else:
		print("You are only allowed to write 1 and 2.")
		menu()

menu()