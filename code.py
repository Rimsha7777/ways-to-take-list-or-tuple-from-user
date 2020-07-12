#ways to take list or tuple from user 
#first method
input_string = input("Enter a list numbers or elements separated by space: ")
userList = input_string.split()
print("user list is ", userList)

print("Calculating sum of element of input list")
sum = 0
for num in userList:
    sum += int(num)
print("Sum = ", sum)
#2nd methood
numberList = []
n = int(input("Enter the list size : "))
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = int(input())
    numberList.append(item)
print("User List is ", numberList)
#3rd methood
n = int(input("Enter the size of list : "))
numList = list(int(num) for num in input("Enter the list numbers separated by space: ").strip().split())[:n]
print("New List: ", numList)
