from todo import ToDoList
from utils import clear_screen, print_divider

def main():
    todo = ToDoList()

    while True:
        print_divider()
        print("📝 TO-DO LIST MANAGER")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            title = input("Enter task title: ").strip()
            if title:
                todo.add_task(title)
            else:
                print("⚠️ Task title cannot be empty.")
        elif choice == '2':
            todo.view_tasks()
        elif choice == '3':
            todo.view_tasks()
            try:
                index = int(input("Enter task number to remove: ")) - 1
                todo.remove_task(index)
            except ValueError:
                print("⚠️ Invalid input. Enter a number.")
        elif choice == '4':
            todo.view_tasks()
            try:
                index = int(input("Enter task number to mark as completed: ")) - 1
                todo.complete_task(index)
            except ValueError:
                print("⚠️ Invalid input. Enter a number.")
        elif choice == '5':
            todo.save_tasks()
            print("✅ Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
