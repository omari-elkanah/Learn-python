print("hello user\n")
names = input("Please enter your name.\n")
gender = input ("Select one for male or two for female.\n")

clothes=["heels","dress","sunhat","sharpshutas","hublot","trucker caps"]
#1 for male 2 for female
if gender == 1:
    gender2 = "male"
    print("alaa")
    print("Hey "+names+" I would reccommend you check out these\n"+str(clothes(3,4,5)))
elif gender == 2:
    gender2 ="female"
    print("waah")
    print("Hey "+names+" I would reccommend you check out these\n"+str(clothes(0,1,2)))
#print("Hey "+names+" I would reccommend you check out these\n"+str(clothes))

suggestions=("heels","dress","sunhat","sharpshutas","hublot","trucker caps")
select= input("\nCare to suggest additions to the list of items?\n y or n \n")
if select == "y":
    suggestions= input("What items would you like to see?")
    select= input("\nCare to suggest other additions to the list of items?\n y or n \n")
    if select== "y":
        suggestions= input("What other additions?")
    else: exit(print("Thank you"))
    print(suggestions)
else:
    exit(print("Thank you"))
print(suggestions)