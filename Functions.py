from Student1 import Student

def multiply(num):
    return num*num*num

def changeList(nums):
    nums[1]=10

def max_of_three(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num3:
        return num2
    else:
        return num3




nums= [1,2,3]
print(multiply(4))
changeList(nums)
print(nums)

print("max of three: ",max_of_three(3, 4, 5))
