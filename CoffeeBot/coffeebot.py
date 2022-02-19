menuitem = ["regular", "decafe", "tea"]

## Greeting and show menu
print("Hello, welcome to the coffee shop! \n")
name = input("What is your name? \n")
print("Hello " + name + ", thank you for comming in. Please take a look at our menu. \n")

## Show each menu item from array 'menuitem'
print ("~~ Menu ~~")
print (menuitem[0])
print (menuitem[1])
print (menuitem[2])

## Evaluate customer's coffee choise
coffeetype = input("\n What can I get you from the menu? \n")
if coffeetype == "regular":
    print ("No problem! We will complete that order and get it to you in under 2 minutes! \n")
    #orderfinish = 1
elif coffeetype == "decafe":
    print ("Ok...so we offer decafe as a litmis test. You can kindly leave and never come back. \n")
    #orderfinish = 2
elif coffeetype == "tea":
    print ("We will absolutly grab you that tea. Please wait roughtly 30-45 minutes for the sourcing of our exculsive tea leaves from the nearby fortune teller. \n")
    #orderfinish = 3
else:
    print ("Please try again! [the barista is heard grumbling] \n\n\n")

## Unsure what to do with 'orderfinish' variable. I had a plan and quickly lost it.
## Would like to add pricing for each item and food items.
## Calcualtor for prices and a recipt would be a nice addition as well.