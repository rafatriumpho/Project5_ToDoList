tasks = []
with open ('Tasks.txt', 'r') as file:
    for line in file:
        tasks.append(line.strip())
print ('Welcome to your To Do List! Press:')
print ('1. Add Item')
print ('2. Remove Item')
print ('3. View List')

while True:
    choice = int(input('\nWhat would you like to do? '))
    if choice == 1:
        newitem = input('New Item: ')
        tasks.append(newitem)
        with open('Tasks.txt', 'w') as file:
            for task in tasks:
                file.write(task + '\n')
            print ('Task added to list successfully!')
    elif choice == 2:
        print ('Your current tasks:')
        counter = 1
        for task in tasks:
            print(f"{counter}. {task}")
            counter += 1
        remove = int(input('Which item do you want to remove from your list? '))
        index = remove - 1
        tasks.pop(index)
        with open('Tasks.txt', 'w') as file:
            for task in tasks:
                file.write(task + '\n')
        print ('Task removed successfully!')
    elif choice == 3:
        print ('Your current tasks:')
        counter = 1
        for task in tasks:
            print(f"{counter}. {task}")
            counter += 1