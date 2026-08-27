import openpyxl
file = openpyxl.load_workbook("C:\\Users\\HP\\Downloads\\pythonDemoExcel.xlsx")

sheet = file.active
cell = sheet.cell(row=1, column=2)
print(cell.value)
#write down to excel
sheet.cell(row=2, column=2).value = "Gabriel"
print(sheet.cell(row=2, column=2).value)
#how much rows in the excel
print(sheet.max_row)
#how much rows in the excel
print(sheet.max_column)
#reveaL VAlue of the specific cell
print(sheet['A5'].value)
#print 1 column date
# for i in range(1, sheet.max_row+1):
#     print(sheet.cell(row=i, column=1).value)

 # print all the date from each column/row
# for i in range(1, sheet.max_row + 1):
#     for j in range(1, sheet.max_column + 1):
#         print(sheet.cell(row=i, column=j).value)
dictionary = {}
#print 3 column and row data Testcase2
for i in range(1, sheet.max_row +1): #to get rows
    if sheet.cell(row=i, column=1).value == "Testcase2":
        for j in range(2, sheet.max_column): #to get columns
            #dictionary['lastname'] = "Ross"
            dictionary[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value

print(dictionary)