def listMethods(lst, choice):
    if choice == 1:
        element = 1
        for i in range(len(lst)):
            print(f"{element}. {lst[element - 1]}")
            element +=1
    elif choice == 2:
        element = 1
        for i in range(len(lst)):
            print(f"{element}. {lst[element - 1]}")
            element +=1
        remItem = int(input('What item would you like to remove? (Type a number) '))-1
        del tasks[remItem]
    elif choice == 3:
        print()
        tasks.append(input("What would you like to add? "))
    
tasks = [
    "Buy groceries",
    "Finish project report",
    "Finish python project",
    "Schedule a dentist appointment",
    "Go for a run"
]
userChoice = 0
print('Welcome to to-do list app!\n')
while userChoice != 4:
    print('(1) Read out your to do list')
    print('(2) Remove an item')
    print('(3) Add an item')
    print('(4) Exit app')
    userChoice = int(input('Choose an option: '))
    listMethods(tasks, userChoice)