class Error(Exception):
    """Raise when any error occurs"""
    pass
class ValueTooSmallError(Exception):
    """Raised when the input value is too small"""
    pass
class ValueTooLargeError(Exception):
    """Raised when the input value is too large"""
    pass



min_number = 20
max_number = 200
while True:
    try:
        i_num=int(input("Enter a number: "))

        if i_num < min_number:
            raise ValueTooSmallError
        elif i_num> max_number:
            raise ValueTooLargeError
        print("Congratulations! You are entered correct value.")
        break

    except ValueTooSmallError:
        print("This value is too small, try again!")
    except ValueTooLargeError:
        print("This value is too large, try again!")
        
    except:
        print("Normal error")
    




        
print(i_num)
