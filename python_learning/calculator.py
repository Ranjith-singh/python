n1= input("Enter number 1: ")
n2= input("Enter number 2: ")
operator= input("Enter the operation: ")
if(not(n1.isalpha()) and not(n2.isalpha())):
    n1= float(n1)
    n2= float(n2)
    if(operator== '+'):
        print(n1+n2)
    elif(operator== '-'):
        print(n1-n2)
    elif(operator== '*'):
        print(n1*n2)
    elif(operator== '/'):
        print(n1/n2)
    elif(operator== '%'):
        print(n1%n2)
    else:
        print("Invalid operator")
else:
    print("Enter only numbers")