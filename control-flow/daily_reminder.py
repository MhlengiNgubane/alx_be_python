task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if priority in ['high', 'medium', 'low'] and time_bound in ['yes', 'no']:
    if time_bound == 'yes':
        reminder_message = f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"
    else:
        reminder_message = f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time."
    print(reminder_message)
else:
    print("Invalid input. Please enter 'high', 'medium', or 'low' for priority and 'yes' or 'no' for time-bound.")