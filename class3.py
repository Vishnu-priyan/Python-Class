kar = ('karthick','Healthy','$200','Global Hospital')
john = ('John','Cancer','$500','Global Hospital')
ram = ('ramesh','Diabetes','$12300','Apollo Hospital')
vel = ('Velayutham','Healthy','FREE','GH Hospital')


#DATABASE SQL READ atha STORE
# -----------
# -----------
# ReaD!!!

name_list = [kar,john,ram,vel]

for item in name_list:
    if item[1]=="Healthy":
        print("CONTINUE happens here")
        continue
    print("""
#---------------------------------#
#   Hello Mr.{0} you have {1}     
#        UNFORTUNATELY          
#    BUT you do have to PAY       
#            {2}                  
#      to  {3}                    
#---------------------------------#""".format(item[0],item[1],item[2],item[3]))
    print("NEXT CUSTOMER")

