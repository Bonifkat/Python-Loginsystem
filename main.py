from yml import data_save_type
from sqliteloginsystem import sqlite_mode
from mysqlloginsystem import mysql_mode



if data_save_type == "SQLITE":
    print("SQLITE MODE")
    sqlite_mode()
elif data_save_type == "MYSQL":
    print("MYSQL MODE")
    mysql_mode()
else:
    print("Data save mode unreadable")