task_list = []

while True:
    print("=== Todo List Menu ===")
    print("1. View Task")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    user_choice = input("Enter your choice: ")


    if user_choice == "1":
        if not task_list:
            print("No tasks yet")
        else:
            print("Your Tasks: ")
            for i, task in enumerate(task_list, start=1):
                print(f"{i}. {task}")

    elif user_choice == "2":
        add_task = input("Enter new task: ")
        task_list.append(add_task)
        print(f"Task added: {add_task}")

    elif user_choice == "3":
        if not task_list:
            print("No tasks to delete")
        else:
            try:
                delete_task = int(input("Enter task number to delete: "))
                if 1 <= delete_task <= len(task_list):
                    removed_task = task_list.pop(delete_task -1 )
                    print(f"Task removed: {removed_task}")
                else:
                    print("Invalid task number")
            except ValueError:
                print("Please enter a valid task number")

    elif user_choice == "4":
        print("Exiting")
        break

    else:
        print("Invalid choice")
        print("Please enter a valid choice")


