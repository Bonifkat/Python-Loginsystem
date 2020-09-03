import yaml
import mysql.connector

with open("test.yml", "r") as s:
    y = yaml.load(s)
    print(y)

##################config-load######################

min_password_length: y["min-password-length"]
data_save_type = y["data-save-type"]
mysql_settings = y["mysql"]
sqlite_settings = y["sqlite"]

##################################################

min_password_length = y["min-password-length"]
data_save_type = y["data-save-type"]

print(min_password_length)
print("-------------------")

if data_save_type == "SQLITE":
    print("SQLITE MODE")
    print(sqlite_settings)
elif data_save_type == "MYSQL":
    print("MYSQL MODE")
    print(mysql_settings)
else:
    print("Data save mode unreadable")

databasemysql = mysql.connector.connect(
  host= mysql_settings["host"],
  user= mysql_settings["user"],
  password=mysql_settings["password"],
  database=mysql_settings["database"]
)

print(mysql_settings["host"])

c = databasemysql.cursor()

c.execute("SELECT username FROM userdata WHERE username = %s", ("Csiga1111",))
