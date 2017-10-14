print("Hey enter some number to add")
try:
    a = int(input("Enter a"))
    b = int(input("Enter b"))
    f = open("asdasdsad.txt")
    c = a+b

    print(c)
except ValueError:
    print("value thappu da")
except FileNotFoundError:
    print("File eh ila da")
finally:
    print("Nan mixture thinmban da")

print("Ok I'm going to tell a important secret")
print("LISTEN")
print("There is money inside our bag. 1 crore rs")
