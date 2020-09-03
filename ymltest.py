import yaml

with open("test.yml", "r") as s:
    y = yaml.load(s)
    print(y)

##################config-load######################

min_password_length: y["min-password-length"]
data_save_type = y["data-save-type"]

##################################################



"""
min_password_length = y["min-password-length"]
data_save_type = y["data-save-type"]

print(min_password_length)
print("-------------------")

if data_save_type == "SQLITE":
    print("SQLITE MODE")
elif data_save_type == "MYSQL":
    print("MYSQL MODE")
else:
    print("Data save mode unreadable")
"""