print("Get maxmimum user info")

name= ''
age = 'NA'

try:
    name = input("Enter name")
    age = int(input("Enter age"))
    
except:
    print("some value is wrong")

finally:
    gps = "chennai"


print("User info")
print(name)
print(age)
print(gps)
