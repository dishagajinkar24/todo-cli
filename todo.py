# To-Do CLI App with Save Feature (Beginner Friendly)

import json
import os

TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

tasks = load_tasks()

def show_menu():
    print("\n==== To-Do Menu ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        print(f"✅ Task added: {task}")

    elif choice == "2":
        if not tasks:
            print("No tasks yet!")
        else:
            for i, t in enumerate(tasks, start=1):
                status = "✔" if t["done"] else "✖"
                print(f"{i}. [{status}] {t['task']}")

    elif choice == "3":
        num = int(input("Enter task number to mark done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print("🎉 Task marked as done!")
        else:
            print("❌ Invalid task number.")

    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice, please try again.")
