def is_divisible(x,y): #the is_divisible function from Section 6.4 of the textbook
    if x%y == 0:
        return True
    else:
        return False

def is_power(a,b): #is_power function that takes two arguments
    if a==b: #the base case of the two arguments being equal
        return True
    elif b==1: #the base case of the second argument being "1"
        if a==1:
            return True
        else:
            return False
    elif is_divisible(a,b) and is_power(a/b,b): #the is_power function call is_divisible and call itself recursively
        return True
    else:
        return False



print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))