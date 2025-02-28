def fancyList(lst):
    element = 1
    for i in range(len(lst)):
        print(f"{element}. {lst[element - 1]}")
        element +=1
        
def options(item, burgers, meals, drinks):
    if item == 1:
        print()
        fancyList(burgers)
        burgerType = int(input("Which burger do you want? "))
        print(f"\nYou ordered a {burgers[burgerType -1]}")

    elif item == 2:
        print("\nYou ordered frys!")

    elif item == 3: 
        print()
        fancyList(meals)
        mealType = int(input("Which meal do you want? "))
        print()
        fancyList(drinks)
        drinkType = int(input("What drink do you want? "))
        print(f"\nYou ordered a {meals[mealType -1]} with a {drinks[drinkType-1]}")

    elif item == 4:
        print()
        fancyList(drinks)
        drinkType = int(input("What drink do you want? "))
        print(f"\nYou ordered a {drinks[drinkType -1]}")
    

    
    if item < 5 and item > 0:
        print('Your order will be out shortly!')

    elif item > 5 and item < 0:
        print('\nPlease choose a valid item!')


menu = ["Burger", "Frys", "Meal", "Drink"]
burgers = ["Cheeseburger", "Hamburger", "Chicken Sandwhich (Halal)"]
meals = ["Cheeseburger Meal", "Hamburger Meal", "Chicken Sandwhich meal (Halal)"]
drinks = ["Water", "Cola", "Sprite", "Orange Soda", "Diet Cola"]


fancyList(menu)
item = int(input("Choose an item number! "))
options(item, burgers, meals, drinks)
