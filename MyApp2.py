def fancyList(lst):
    element = 1
    for i in range(len(lst)):
        print(f"{element}. {lst[element - 1]}")
        element +=1
    return ""
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
    
    if userChoice == 1:
        print()
        print(fancyList(tasks))
    if userChoice == 2:
        print()
        print(fancyList(tasks))
        remItem = int(input('What item would you like to remove? (Type a number) '))-1
        del tasks[remItem]
    if userChoice == 3:
        print()
        tasks.append(input("What would you like to add? "))