from con1 import *
connect(password="root", database="FullStack")
createTable("users1",name="string", age="int")
def greeting(name):
    print(f"Hello, {name}!")
    print("Welcome to the Django ORM example.")
    print("This is a simple demonstration of how to create tables and insert data using Python.")
    print("Feel free to explore and modify the code as needed.")
# insertOne("users1", "John Doe", 30)
# insertOne("users1", "Jane Smith", 25)   
# insertOne("users1", "Alice Johnson", 28)  
# insertOne("users1", "Bob Brown", 35)
# findall("users1")               
# findById("users1", 2)

pre(greeting, "users1")
insertOne("users1", "Charlie Davis", 22)      