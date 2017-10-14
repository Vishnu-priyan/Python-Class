kar = ('karthick','Healthy','$200','Global Hospital')
john = ('John','Cancer','$500','Global Hospital')
ram = ('ramesh','Diabetes','$12300','Apollo Hospital')
vel = ('Velayutham','Healthy','FREE','GH Hospital')

name_list = [kar,john,ram,vel]

for item in name_list:
    if item[1]=="Healthy":
        pass
    else:
        print(item[0])









not_healthy_list = [item[0] for item in name_list
                    if item[1]!="Healthy"]
















a = ['R.vijay','S.karthick','V.vimala']
final = [(item[0],item[2:]) for item in a]

for item in a:
    a = item[0]
    b = item[2:]
    temp = (a,b)
    final.append(temp)































'''age = [12,33,35,67,88]




namelist = ['karth','joHn','ram','raJEs','RAkesh','ragu']




final_lc = [[item[0],item.upper(),item.lower()] for item in namelist]


final_nor = []
for item in namelist:
    a = item[0]
    b = item.upper()
    c = item.lower()
    temp = (a,b,c)
    final_nor.append(temp)

'''
