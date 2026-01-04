"""#  venv ->VENV ka full form hai Virtual Environment.
# Ye Python ka ek tool/package hota hai jo alag-alag projects ke liye alag environment banata hai. 
# VENV ek box jaisa hota hai jisme:
# Python
# Libraries / packages
# sirf usi project ke liye install hote hain.
# Problem bina VENV ke 
# Ek project ko Django==3.2 chahiye
# Dusre project ko Django==4.2 chahiye
# Dono same system Python me install karoge to conflict hoga.
# Solution: 
# Har project ka alag virtual environment
# Packages ek-dusre se conflict nahi karte
# ENV ka use kyun karte hain?
# ✔ Package version conflict avoid
# ✔ Project clean & professional
# ✔ Industry standard practice
# ✔ Same system me multiple projects safely
# pip install virtualenv
# python -m venv .venv (.venv virtual envirnment ka naam h )
# ls
# dir
# ls -Force
# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -> execution policy ko enabled kr rhe h (permission le rhe h)
#  Command line interpreter pr:
# cd C:\Users\indu2\Music\Music\Web-Development\Web-Development\Full_Stack_Python\VirtualEnvironment
# .venv\Scripts\activate.bat
# 
(.venv) C:\Users\indu2\Music\Music\Web-Development\Web-Development\Full_Stack_Python\VirtualEnvironment>python --version
Python 3.13.0

(.venv) C:\Users\indu2\Music\Music\Web-Development\Web-Development\Full_Stack_Python\VirtualEnvironment>pip list
Package Version
------- -------
pip     24.2

(.venv) C:\Users\indu2\Music\Music\Web-Development\Web-Development\Full_Stack_Python\VirtualEnvironment>
# >pip install pymongo #  ye virtual environment me hua h system me nhi
(.venv) C:\Users\indu2\Music\Music\Web-Development\Web-Development\Full_Stack_Python\VirtualEnvironment>pip list
Package   Version
--------- -------
dnspython 2.8.0
pip       24.2
pymongo   4.15.5


pip freeze > requirements.txt
🔹 pip install -r requirements.txt ka matlab

1 pip → Python ka package manager (jo packages install karta hai)
2 install → batata hai ki package install karna hai
3 -r requirements.txt → “read from file” flag, matlab jo packages requirements.txt me listed hain, unhe install karo
python -m pip install django
"""


