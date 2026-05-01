
import mysql.connector

db_con_obj = mysql.connector.connect(
    host="localhost",
    user="root",
    database="my_oops_project",
    password="Nani@2703"
)
cur_obj = db_con_obj.cursor()
print("database connected")


