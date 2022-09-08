from openpyxl import Workbook , load_workbook


def add_data(list_data):
   ws = load_workbook('work.xlsx')
   wa = ws.active
   wa.append(list_data)
   ws.save("work.xlsx")
   


def auto_id():
   ws = load_workbook('work.xlsx')
   wa = ws.active
   id_list=[]
   for row in range(1,len(wa['A'])+1):
      # print(wa['A'+str(row)].value)
      id_list.append(int(wa['A'+str(row)].value))
      # print(wa['A'+str(row)].value , type(wa['A'+str(row)].value))
   return id_list   


