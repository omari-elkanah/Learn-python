#print("Hello world")
name = input("what is your name?\n")

if name == "ben" or "Ben" or "BEN" or "BeN":
    print("You are not welcome")
    exit()
else:
    print("Hello "+ name +", welcome")
    menu="Coffee, Milk, Juice, ALKOHOL" 
    print("\n\nThese are the items on today's menu. Pick one\n" +menu)
    order= input()
    print("\nExcellent choice.\n")
    print("\nWhat quantity of "+ order +" will you take?")
   
    amount=input()
    if order == "coffee":
        coffee_status =input("Black or white?")
        if coffee_status == "black":
            price = 80
        elif coffee_status == "white":
            price = 100
        else: exit()
    elif order == "milk":
        price = 90
    elif order == "juice":
        juice_status = input("Big or small?\n")
        if juice_status == "big":
            price = 100
        elif juice_status=="small":
            price =60
        else: exit()
    elif order == "alkohol":
        alkohol_status = input("Do you want it with lemon? yes or no\n")
        if alkohol_status == "yes":
            price = 1600
        elif alkohol_status == "no":
            price = 1500
        else: exit()
    else:
        exit("thank you")
    total =int(amount)*price
    print("Your total amount of "+ order +" "+amount+" is priced at "+str(total)+"")
    exit()