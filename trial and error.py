print("Welcome")
name = input("What is your first name?\n")
name2 = input("Enter your second name\n")
no =input("Pick 1 or 2\n")
if not int(no)== 1 or int(no)== 2:
    exit()
print("Hey "+name + name2+" you picked "+no)