import mysql.connector
conn = mysql.connector.connect(user='root', password='ver64pad', host='localhost', database='db1907')
mycursor = conn.cursor()
mycursor.execute("Show Tables")
print mycursor.fetchall()
