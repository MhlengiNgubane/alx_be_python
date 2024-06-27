task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case 'high':
        print(f"Reminder: {task} is a high priority")
        if time_bound == 'yes':
            print("task that requires immediate attention today!")
        else:
            print("This task does not have an immediate deadline.")
    case 'medium':
        print(f"Task: {task} has medium priority.")
        if time_bound == 'yes':
            print("This task is time-bound and requires attention soon.")
        else:
            print("This task does not have an immediate deadline.")
    case 'low':
        print(f"Task: {task} has low priority.")
        if time_bound == 'yes':
            print("This task is time-bound but may be addressed later.")
        else:
            print("This task does not have an immediate deadline.")
    case _:
        print(f"Invalid priority: {priority}. Please enter 'high', 'medium', or 'low'.")