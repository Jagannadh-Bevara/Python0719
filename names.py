import mysql.connector

conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='db1907')
mycursor = conn.cursor()
mycursor.execute("Show Tables")
print mycursor.fetchall()
