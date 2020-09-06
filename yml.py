import bcrypt
import sqlite3
import mysql.connector
import yaml

with open("test.yml", "r") as s:
    yml_import = yaml.safe_load(s)

##################config-load######################

min_password_length: yml_import["min-password-length"]
data_save_type = yml_import["data-save-type"]
mysql_settings = yml_import["mysql"]
sqlite_settings = yml_import["sqlite"]

##################################################
























