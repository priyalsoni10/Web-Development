import mysql.connector
con = ""
cursor = ""
def  connect(**args): # function to connect to the database
    global con
    global cursor
    host =args.get('host', 'localhost')
    user =args.get('user', 'root')
    password =args.get('password')     
    database =args.get('database')
    try:
        con = mysql.connector.connect(
            host=host,
            user=user,
            password=password,    
            database=database
        )
        print("Successfully connected to database...")
        cursor = con.cursor()
    except Exception as e:
        print("Failed to Database Connectivity ...",e)
preTableName = ""
fun = ""
def pre(func, tableName):
    global preTableName
    global fun  
    preTableName = tableName
    fun = func
    # print("Pre function called...")
    # func()
DataTypes = {
            "int": "int",
            "string": "varchar(255)",
            "float": "float",
            "date": "date"
        }
        
ColNames = ()    
def createTable(TName,**cols):
  global ColNames
  query = f"CREATE TABLE IF NOT EXISTS {TName} ( id INT AUTO_INCREMENT PRIMARY KEY, "
  for colName ,j in cols.items():
    # print(colName, DataTypes.get(j))
    if colName == "id" or colName == "Id":
        continue
    dType = DataTypes[j]
    query += f"{colName} {dType},"
    ColNames += (colName,)

  query = query[:-1]    # Remove the last comma and add closing parenthesis
  query += ");"
  print(query)
  try:
    cursor.execute(query)
    con.commit()
    print("Table created successfully.")
  except Exception as e:
    print("Error creating table:", e)


def insertOne(TName,*values):
    # placeholders = ", ".join(["%s"] * len(values))
    query = f"INSERT INTO {TName} ({','.join(ColNames)}) VALUES {values};"
    if preTableName == TName:
        fun(values[0])
    try:
        # print(query) 
        cursor.execute(query)
        con.commit()
        print("Data inserted successfully.")
    except Exception as e:
        print("Error inserting data:", e)
        
        
def findall(TName):
    query = f"SELECT * FROM {TName};"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
        # return results
    except Exception as e:
        print("Error fetching data:", e)
def findById(TName, id):
    query = f"SELECT * FROM {TName} WHERE id = {id};"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
        # return results
    except Exception as e:
        print("Error fetching data:", e)

        
        