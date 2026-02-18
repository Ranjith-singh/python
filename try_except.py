try:
    value= 10/0
    num= int(input("Enter the number: "))
except ValueError as value_error:
    print("Invalid input")
except ZeroDivisionError as div_zero:
    print(div_zero)