from openpyxl import Workbook , load_workbook
from add import add_data , auto_id

while True:
   
   username = input("Enter  username:")
   password=input("enter password ")
   camount = int(input("Enter you amount:"))
   print(max(auto_id()))

   auto_id = auto_id() 
   # list_data = [username,password,camount]
   # add_data(list_data)
   
   check= input("Do you want yo enter data again? y/n ")
   if check == 'n' :
      break


print("ol")



print("hi there")
# Hello everyone