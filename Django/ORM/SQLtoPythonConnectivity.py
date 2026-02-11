import mysql.connector
con = mysql.connector.connect(
  host="localhost",
  user="root" ,
  password="",
  database="FullStack"
)
# print(con)
cursor = con.cursor()
cursor.execute("SELECT * FROM users")
for i in cursor:
    print(i)

def getData(tableName):
    cursor.execute("SELECT * FROM " + tableName)
    data = cursor.fetchall()
    return data
print(getData("users"))

# def insertData(tableName, data):
#     cursor.execute("INSERT INTO " + tableName + " VALUES (" + data + ")")
#     con.commit()  # Commit the transaction to save changes to the database  
# data = "7,'Jennal','jennal@gmail.com','653341','6789556475', 'Jodhpur ,Rajasthan' ,'1989-09-28' , 'F', 0"
# insertData("users", data)
# getData("users")
