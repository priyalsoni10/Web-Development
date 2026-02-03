"""
FileHandling:
File handling ka matlab hota hai file ko read, write, update aur close karna.
Python me mainly open() function use hota hai
Mode	Meaning
r	Read (default)
w	Write (purana data delete ho jata hai)
a	Append (data end me add hota hai)
x	Create new file
r+	Read + Write
w+	Write + Read
a+	Append + Read
"""
#  Create File
# f1 = open("FileHandling2.py","x")  # create new file 
# Read File
f1 = open("FileHandling2.py","r")  # read existing file 
data = f1.read()
print(data)
print("-----------------")

#  Write File
# f1 = open("FileHandling3.py","w")  # craete new file if not exist and if exist overwrite content
f2 = open("FileHandling2.py","w") # content write kr skte h
data1 = f2.write("# Welcome to Learning the concept of File Handling") # previse content overwrite ho gya
print(data1) # 48 words with spaces
print("-------------------")

# (r+)-> Read and Write in existing file (isme read phle krna h fir write krna )
f3 = open("FileHandling2.py","r+") # read and write only in existing file
print(f3.read())
data1 = f3.write("# Welcome to Learning the concept of File Handling") # previse content overwrite ho gya
# print(data1) # phle write or fir read keya to cursor beginning me rhega to use ke upper overwrite krta chalega(Welcome->Hilcome ho jaega modify hone pr uske baad read keya to cursor do word aage point hogaa ->lcome)
print(f3.tell()) # 48 index pr h cursor abhi 
print("-------------------")

# (w+) -> create new file if not exist and also write  and read File (isme phle write fir read) 
f4 = open("FileHandling2.py","w+") # read and write only in existing file
print(f4.tell()) # 0 index
f4.write("# Welcome to Learning the concept of File Handling ") # previse content overwrite ho gya
print(f4.tell()) # 49
f4.write("This is Python") # previse content overwrite ho gya
f4.seek(0) # cursor ko fir 0 index pr  lane keleye
print(f4.tell()) # 0
data4 =  f4.read()
# print(data4) # data print nhi kr pa rha h kyonki cursor last me h isse kuch print nhi ho rha h 
print(data4)
# print(f4.tell()) # 63 
print(f4.tell()) # 0 
# print(data1) # phle write or fir read keya to cursor beginning me rhega to use ke upper overwrite krta chalega(Welcome->Hilcome ho jaega modify hone pr uske baad read keya to cursor do word aage point hogaa ->lcome)
print("-------------------")

# Append -> file ke last me append krta h (overwrite nhi krta) or file exist nhi krte to create bhi krta h  read nhi kr skte
f5 = open("FileHandling2.py","a") # sirf write krskte h data readsd nhi kr skte
f5.write(" Wow!!")
# print(f1.read()) # error
 # Append (a+) -> file ke last me append krta h (overwrite nhi krta) or file exist nhi krte to create bhi krta h
f6 = open("FileHandling2.py","a+") # cusor last me rehta hto kuch print nhi krta 
data = f6.write("\n # It's interesting")
print(f6.tell()) # 86
f6.seek(0)
print(f6.read(data)) 
f6.write("\n #Learn By Fun")

# Binary File  -> rb
f6 = open("FileHandling2.py","rb") # for binaary file like images  read mode
f7   = open("FileHandling2.py","wb") # for binaary file like images  right mode
for i in f6:
    f7.write(i) # jo file content f6 mee h vo f7 me bhi aajaega
print(f6.read()) 