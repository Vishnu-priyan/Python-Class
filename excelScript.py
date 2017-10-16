import openpyxl
ex_doc = openpyxl.load_workbook('sample.xlsx')
sheet = ex_doc.get_sheet_by_name('Sheet1')



def final_salary(tup):
    if tup[2] > 8:
        extra_hrs = tup[2]-8
        amount = extra_hrs*39
        final = tup[0] + amount
        return final
    elif tup[2] < 8:
        left_hrs = 8 - tup[2]
        amount = left_hrs*39
        final = tup[0] - amount
        return final
    else:
        final = tup[0]
        return final  




multiple_rows = sheet['A1':'D7']


baseSalary = []
name = []
shift = []
days = []
for item in multiple_rows:
    baseSalary.append(item[0].value)
    name.append(item[1].value)
    
    shift.append(item[2].value)
    days.append(item[3].value)


a = list(zip(baseSalary,name,shift,days))
final_salary_list = []
for i,item in enumerate(a):
    if i==0:
        pass
    else:
        final_salary_list.append(final_salary(item))



        
