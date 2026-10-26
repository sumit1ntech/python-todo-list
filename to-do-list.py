# =================================
# To-Do List App
# Description: A simple task management application built with Python.
# Features: Add, view, complete, and delete tasks.
# Concepts: Lists, loops, match-case, and conditional statements.
# Author: Sumit Bhaya | @sumit1ntech
# =================================
tasks = []
completed_tasks = []
while True:
    print("===== TO-DO LIST =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")
    user_choice = int(input("Choice: "))

    match user_choice:
        case 1:
            user_task = input("Enter Your Task: ")
            tasks.append(user_task)
        case 2:
            print(tasks)
        case 3:
            for i in range(len(tasks)):
                print(i+1, tasks[i])
            num = int(input("Enter Task Number: "))

            if 1 <= num <= len(tasks):
                completed_tasks.append(tasks.pop(num-1))
                print(f"{num} of task is completed")
            else:
                print("Invalid task number")
        case 4:
            for i in range(len(tasks)):
                print(i+1, tasks[i])
            num = int(input("Enter Task Number: "))

            if 1 <= num <= len(tasks):
                tasks.pop(num-1)
                print(f"{num} of Task deleted!")
            else:
                print("Invalid task number")
        case 5:
            print("Thank you for using my To-Do List App!")
            print("Stay productive. Have a great day!")
            exit()
            break
            break