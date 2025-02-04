# To-Do List
import os # Import for file handling

tasks = [] # List to store tasks

def load_tasks():
    """Load tasks from a file when the program starts."""
    if os.path.exists("tasks.txt"): # if file exists, read it
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip()) # remove extra spaces

def save_tasks():
    """Save the tasks to a file."""
    with open("tasks.txt", "w") as file: # open in write mode
        for task in tasks:
            file.write(task + "\n") # write each task on a new line

def show_tasks():
    if not tasks:
        print("No task available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("\nEnter new task:")
    tasks.append(task)
    print(f"Task {task} added.")

def remove_task():
    try:
        task_num = int(input("Which task do you want to remove?")) - 1
        show_tasks()
        if 0 <= task_num <= len(tasks) - 1:
            removed_task = tasks.pop(task_num)
            print(f"Task {removed_task} removed")
        else:
            print("Enter a valid task number.")
    except ValueError:
        print("Please enter a valid task number.")

def main():
    load_tasks() # load existing tasks on startup
    print("Welcome to the To-Do List App!")
    while True:
        print("\nTo-Do List Options:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
            save_tasks()
        elif choice == "3":
            remove_task()
            save_tasks()
        elif choice == "4":
            print("\nExiting... Have a productive day!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()