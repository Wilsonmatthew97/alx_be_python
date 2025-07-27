task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
reminder = f"'{task}' is a {priority} priority task"
match priority:
    case "high":
        if time_bound == "yes":
            message = "that require immediate attention today!"
            print(f"Reminder: {reminder} {message}")
        elif time_bound == "no":
            message = "But you have time to finish the task."
            print(f"Reminder: {reminder}. {message}")
    case "medium":
        if time_bound == "yes":
            message = "that requires attention, time is running out."
            print(f"Reminder: {reminder} {message}")
        elif time_bound == "no":
            message = "But you can complete it in your free time."
            print(f"Reminder: {reminder}. {message}")
    case "low":
        if time_bound == "yes":
            message = "Time is running out!"
            print(f"Reminder: {reminder}. {message}")
        elif time_bound == "no":
            message = "Consider completing it in your free time."
            print(f"Reminder: {reminder}. {message}")
    case _:
        reminder = f"incorrect input!"
        print(reminder)
