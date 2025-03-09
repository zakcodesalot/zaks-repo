import os

# Function to load tasks from a file
def load_tasks(filename="tasks.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    else:
        return []

# Function to save tasks to a file
def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to display the tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Main program function
def to_do_list_app():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == '1':  # Add Task
            task = input("Enter the task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print(f"Task '{task}' added successfully.")
            else:
                print("Task cannot be empty.")

        elif choice == '2':  # View Tasks
            display_tasks(tasks)

        elif choice == '3':  # Mark Task as Done
            display_tasks(tasks)
            try:
                task_num = int(input("Enter task number to mark as done: ").strip())
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1] = tasks[task_num - 1] + " (Done)"
                    save_tasks(tasks)
                    print(f"Task {task_num} marked as done.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':  # Delete Task
            display_tasks(tasks)
            try:
                task_num = int(input("Enter task number to delete: ").strip())
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"Task '{removed_task}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '5':  # Exit
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
