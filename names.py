import mysql.connector
conn = mysql.connector.connect(user='root', password='ver64pad', host='localhost', database='entransys1')
mycursor = conn.cursor()
mycursor.execute("Show Tables")
print mycursor.fetchall()
print("Hello")