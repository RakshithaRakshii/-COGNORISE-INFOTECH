tasks = []

def show_menu():
    print("Todo List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

def add_task():
    task_name = input("Enter task name: ")
    due_date = input("Enter due date (optional): ")
    priority = input("Enter priority (low, medium, high): ")
    task = {"name": task_name, "due_date": due_date, "priority": priority, "completed": False}
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['name']} - Due: {task['due_date']} - Priority: {task['priority']} - Completed: {task['completed']}")

def mark_task_completed():
    view_tasks()
    task_index = int(input("Enter the number of the task to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number!")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
