tasks = [
    {"text": "Buy bread", "done": False},
    {"text": "Do exercises", "done": False}
]
while True:
    print("menu")
    print("1 - Show tasks")
    print("2 - Add task")
    print("3 - Mark task as done")
    print("4 - Exit")
    choice = input('Your choice')
    if choice == "1":
        if not tasks:
            print('No tasks')
        else:
            for i, task_item in enumerate(tasks, start=1):
                status = "-" if task_item["done"] else " "
                print(f"{i}. [{status}] {task_item['text']}")
    elif choice == "2":
        task_text = input("enter a task:")
        tasks.append({"text": task_text, "done": False})
        print("Task added!")
    elif choice == "3":
        num = int(input("Enter the number of the task to mark as done: "))
        if num < 1 or num > len(tasks):
            print("Invalid task number!")
        else:
            tasks[num - 1]["done"] = True
            print(f"Task {num} completed!")


    elif choice == "4":
        print("Exiting program!")
        input("Press Enter to exit")
        break