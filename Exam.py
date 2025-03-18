def options(item, burgers, meals, drinks):
    if item == 1:
        print()
        element = 1
        for i in range(len(burgers)):
            print(f"{element}. {burgers[element - 1]}")
            element +=1
        burgerType = int(input("Which burger do you want? "))
        print(f"\nYou ordered a {burgers[burgerType -1]}")

    elif item == 2:
        print("\nYou ordered Frys!")

    elif item == 3: 
        print()
        element = 1
        for i in range(len(meals)):
            print(f"{element}. {meals[element - 1]}")
            element +=1
        mealType = int(input("Which meal do you want? "))
        print()
        element = 1
        for i in range(len(drinks)):
            print(f"{element}. {drinks[element - 1]}")
            element +=1
        drinkType = int(input("What drink do you want? "))
        print(f"\nYou ordered a {meals[mealType -1]} with a {drinks[drinkType-1]}")

    elif item == 4:
        print()
        element = 1
        for i in range(len(drinks)):
            print(f"{element}. {drinks[element - 1]}")
            element +=1
        drinkType = int(input("What drink do you want? "))
        print(f"\nYou ordered a {drinks[drinkType -1]}")
    

    
    if item < 5 and item > 0:
        print('Your order will be out shortly!')

    elif item > 4 or item < 1:`
        pr`int('\nPlease choose a valid item!')


menu = ["Burger", "Frys", "Meal", "Drink"]
burgers = ["Cheeseburger", "Hamburger", "Chicken Sandwich (Halal)"]
meals = ["Cheeseburger Meal", "Hamburger Meal", "Chicken Sandwich meal (Halal)"]
drinks = ["Water", "Cola", "Sprite", "Orange Soda", "Diet Cola"]


element = 1
for i in range(len(menu)):
    print(f"{element}. {menu[element - 1]}")
    element +=1
item = int(input("Choose an item number! "))
options(item, burgers, meals, drinks)