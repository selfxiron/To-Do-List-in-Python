# To-Do List
import os # Import for file handling

tasks = [] # List to store tasks

def load_tasks():
    """📥 Load tasks from a file when the program starts."""
    if os.path.exists("tasks.txt"):  # Check if file exists
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())  # Remove extra spaces

def save_tasks():
    """💾 Save the tasks to a file."""
    with open("tasks.txt", "w") as file:  # Open in write mode
        for task in tasks:
            file.write(task + "\n")  # Write each task on a new line

def show_tasks():
    """📜 Display all tasks."""
    if not tasks:
        print("\n📜 No tasks available. Add some to stay productive! ✅")
    else:
        print("\n📌 Your To-Do List:")
        print("📝" + "-" * 30)
        for index, task in enumerate(tasks, start=1):
            print(f"  {index}. {task} ")
        print("📝" + "-" * 30)

def add_task():
    """➕ Add a new task."""
    task = input("\n✍  Enter new task: ")
    tasks.append(task)
    print(f"✅ Task '{task}' added successfully! 🚀")

def remove_task():
    """❌ Remove a task."""
    show_tasks()
    try:
        task_num = int(input("🗑 Enter the task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"✅ Task '{removed_task}' removed successfully! 🗑")
        else:
            print("⚠️  Task number out of range. Please enter a valid number.")
    except ValueError:
        print("⚠️  Please enter a valid task number.") 

def edit_task():
    """✏️ Edit an existing task."""
    show_tasks()
    try:
        task_num = int(input("Which task do you want to edit?")) - 1
        if 0 <= task_num < len(tasks):
            edited_task = input("✍  Enter the updated task:")
            tasks[task_num] = edited_task
            print("✅ Task updated successfully! 📝")
        else:
            print(f"⚠️ Task number {task_num + 1} is out of range. Please enter a number between 1 and {len(tasks)}.")
    except ValueError:
        print("⚠️ Please enter a valid task.")
    

def main():
    load_tasks() # load existing tasks on startup
    print("\n🎯 Welcome to the To-Do List App! Stay organized and productive! 🚀")
    while True:
        print("\n📌 To-Do List Options:")
        print("1️⃣  View Tasks 📜")
        print("2️⃣  Add Task ➕")
        print("3️⃣  Remove Task ❌")
        print("4️⃣  Edit Task ✏️")
        print("5️⃣  Exit 🚪")

        choice = input("\nEnter your choice (1-5): ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
            save_tasks()
        elif choice == "3":
            remove_task()
            save_tasks()
        elif choice == "4":
            edit_task()
            save_tasks()
        elif choice == "5":
            print("\n👋Exiting... Have a productive day! 🎯")
            break
        else:
            print("⚠️  Invalid choice, please try again.")

if __name__ == "__main__":
    main()