task = input("Add a task description: ")
priority = input("What's the task's priority? (high, medium, low): ")
match priority:
    case _:
        print("Your selection is not among the list (high/medium/low)")
        priority = input("What's the task's priority? (high, medium, low): ")
time_bound = input("Is this task time bound? (yes or no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time")
    case _:
        print("Your selection is not among the list (high/medium/low)")