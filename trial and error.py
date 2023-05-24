print("Welcome")
name = input("What is your first name?\n")
name2 = input("Enter your second name\n")
no =input("Pick 1 or 2\n")
if int(no)< 1 or int(no)> 2:
    exit()
print("Hey "+name + " "+name2+" you picked "+no)

stuff=["jobs"]
stuff.append(("life"))
stuff.extend(("vacancies","pay"))
stuff = stuff+["cars"]
stuff.insert(2, "umbwa")
stuff.insert(-1, "bidet")
print(stuff)

stuff.remove("pay")
print(stuff)
print(stuff.pop(1))
print(stuff)
print("You removed "+stuff.pop(1))
print("You removed "+stuff.pop(1))
print("You removed "+stuff.pop(1))
print(stuff)
stuff.clear()
print(stuff)