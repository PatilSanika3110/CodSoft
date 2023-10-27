import json
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter task title: ")
    new_task = {"title": title, "done": False}
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' task added successfully")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{removed_task['title']}' Task removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            print("\t")
            print(f"{index}. {task['title']} - {'Done' if task['done'] else 'Not Done'}")
            
def mark_done(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter the number of the task to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['done'] = True
            save_tasks(tasks)
            print(f"Task '{tasks[index]['title']}' done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
        
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Mark Task as Done")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            show_tasks(tasks)
        elif choice == '4':
            mark_done(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please choose a valid option.")
if __name__ == "__main__":
    main()