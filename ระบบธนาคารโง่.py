import time as tm #time set
import random #random

user = input("Enter Name: ")
password = input("Enter password: ")

tm.sleep(2)


if user == "ttmm2352th" and password == "1234" :
    print("Account sucess")
    tm.sleep(2)
    random_number = random.randint(1,1000)
    tm.sleep(2)
    Service = input(f"wait service ticket {random_number} ")
    
else:
    print("Not process")
