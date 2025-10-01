from typing import List, Optional, Union

todo_list: List[str] = []

def show_tasks():
    if not todo_list:
        return "No tasks yet."
    else:
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")
        return todo_list

def add_task(task):
    todo_list.append(task)
    print("Task added.")

def delete_task(task_index):
    try:
        idx = task_index - 1
        if 0 <= idx < len(todo_list):
            removed = todo_list.pop(idx)
            print(f"Deleted: {removed}")
            return removed
        else:
            print("Invalid task number.")
            return None
    except (ValueError, TypeError):
        print("Invalid task number.")
        return None

while True:
    print("\n=== TO-DO LIST ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        show_tasks()
    elif choice == '2':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '3':
        show_tasks()
        try:
            idx = int(input("Enter task number to delete: "))
            delete_task(idx)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid option.")