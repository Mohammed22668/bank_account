from openpyxl import Workbook , load_workbook

def add_data(list_data):
   ws = load_workbook('work.xlsx')
   wa = ws.active
   wa.append (['account id','account name','user name','password','current balance','deposit','withdraw'])
   wa.append(list_data)
   ws.save("work.xlsx")
   
while True:
   username = input("Enter  username:")
   password=input("enter password ")
   camount = int(input("Enter you amount:"))
   
   list_data = [username,password,camount]
   add_data(list_data)
   
   check= input("Do you want yo enter data again? y/n ")
   if check == 'n' :
      break


