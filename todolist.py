# Assignment - TodoList
# Dan Ochs     11/11/2019
#
# present user with menu
# Press 1 to add task
# Press 2 to delete task
# Press 3 to view all tasks
# Press q to quit
#
# Add task
#   ask user for 'title' and 'priority' (high, medium, or low)
# Delete task
#   show user list along with index number,
#   user can enter index number to delete task
# View all tasks
#   allow user to view all tasks in this format:
#   1 - Wash the car - high
#   2 - Mow the lawn - low
#
# store each task in a dictionary, use 'title' and 'priority' as keys
# store each dictionary in a list, this list represents the list of tasks

from os import system

tasks = []

system('clear')

# main program loop
while True:
    print()
    print('Press 1 to add task')
    print('Press 2 to delete task')
    print('Press 3 to view all tasks')
    choice = input('Press q to quit  ')
    if choice == '1':
        # add a task
        title = input('Task title: ')
        while True:
            priority = input('Task priority: ')
            if priority in ['high', 'medium', 'low']:
                break
            else:
                print(f"Priority cannot be {priority}. Please enter high, medium, or low.")
        task = {'title': title, 'priority': priority}
        tasks.append(task)

    elif choice == '2':
        # delete a task    
        # first show the tasks
        for i in range(len(tasks)):
            print(i+1,' - ',tasks[i]['title'],' - ',tasks[i]['priority'])
        # get a task to delete
        try: 
            n = int(input("Enter task number to delete: "))
        except:
            print("Not a valid input.")
            continue
        else:
            if n > 0 and n < len(tasks)+1:
                #delete selected task
                del tasks[n-1]
            else:
                print("Not a valid input.")
                continue

    elif choice == '3':
        # view the tasks
        for i in range(len(tasks)):
            print(i+1,' - ',tasks[i]['title'],' - ',tasks[i]['priority'])            
    elif choice == 'q':
        # quit program
        break
    else:
        # user entered invalid choice
        print(f"{choice} is not an option.")



            
