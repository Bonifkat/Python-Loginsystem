import bcrypt
import sqlite3
import yaml
from yml import sqlite_settings
from yml import yml_import
from yml import min_password_length

def sqlite_mode():
	#name of the database file (userdatabase.db)
	sqliteconn = sqlite3.connect(yml_import["sqlite"])
	conn_sqlite = sqliteconn.cursor()

	#Creates SQLite file if missing.
	conn_sqlite.execute('CREATE TABLE IF NOT EXISTS userdata(username REAL, password REAL)')

	#registration
	def register_sqlite_mode():

		#Visual stuff
		print("----Registeration----")

		username_register_input = input("Username: ")
		password_register_input = input("Password: ")
		password_register_confirm_input = input("Password confirm: ")

		#Check if password length is longer than xy characters.
		if len(password_register_input) >= min_password_length:

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
						conn_sqlite.execute("SELECT username FROM userdata WHERE username = ?", (username_register_input,))

						usernames_from_db = 0
						for checkusername in conn_sqlite.fetchall():
							usernames_from_db = checkusername[0]

						#Checks if username already exists in the database and if not create user.
						if usernames_from_db != username_register_input:
							#Database upload
							conn_sqlite.execute("INSERT INTO userdata (username, password) VALUES (?, ?)",
								(username_register_input, hashed_registered_password))
							sqliteconn.commit()

							#Registration Success message.
							print("------------------------")
							print("Registration Successful!")
							print("------------------------")
							menu_sqlite_mode()

						else:
							#Error message for username already taken.
							print("------------------------")
							print("Registration failed!\nUsername already has been taken.")
							print("------------------------")
							register_sqlite_mode()
					else:
						#Error message for password and password comfirm don't match.
						print("------------------------")
						print("Registration failed!\nPassword didn't match.")
						print("------------------------")
						register_sqlite_mode()

				else:
					#Error message for password not alphanumeric.
					print("------------------------")
					print("Registration failed!\nYou can only use alphanumeric characters.")
					print("------------------------")
					register_sqlite_mode()

					
			else:
				#Error message for username not alphanumeric.
				print("------------------------")
				print("Registration failed!\nYou can only use alphanumeric characters.")
				print("------------------------")
				register_sqlite_mode()
		

		else:
			#Error message for password too short.
			print("------------------------")
			length_error = "Registration failed!\nPassword has to be longer than {0} characters."
			print(length_error.format(min_password_length))
			print("------------------------")
			register_sqlite_mode()

	#login
	def login_sqlite_mode():

		password_login_input = b""

		print("----Login----")
		loginname_login_input = input("Username: ")
		password_login_input = input("Password: ").encode('utf-8')

		#Take hashed password from user
		gethashed = conn_sqlite.execute("SELECT password FROM userdata WHERE username = ?", (loginname_login_input,))

		password_import_from_db = b""
		for password_import_from_db in conn_sqlite.fetchall():
			password_from_db = password_import_from_db[0]

		try:
			#check if the password is the same as the hashed one
			if bcrypt.checkpw(password_login_input, password_from_db.encode('utf8')):
				#Login Success.
				print("------------------------")
				print("Login Successful!")
				print("------------------------")
				menu_sqlite_mode()

			else:
				#Error for wrong password.
				print("------------------------")
				print("Login failed!\nWrong username or password.")
				print("------------------------")
				login_sqlite_mode()

		except:
			#Error for wrong username.
			print("------------------------")
			print("Login failed!\nWrong username or password.")
			print("------------------------")
			login_sqlite_mode()

	#Menu
	def menu_sqlite_mode():

		menu = input("Registration(1), Login(2): ")

		#Registration menu
		if menu == "1":
			register_sqlite_mode()

		#Login menu
		elif menu == "2":
			login_sqlite_mode()

		#Error for pressing anything else than the key 1 and 2.
		else:
			print("You are only allowed to write 1 and 2.")
			menu_sqlite_mode()

	menu_sqlite_mode()

