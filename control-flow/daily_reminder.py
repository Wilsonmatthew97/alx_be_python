task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"'{task}' is a {priority} priority task that require immediate attention today!"
            print(reminder)
        elif time_bound == "no":
            reminder = f"'{task}' is a {priority} priority task. But you have time to finish the task."
            print(reminder)
    case "medium":
        if time_bound == "yes":
            reminder = f"'{task}' is a {priority} priority task that requires attention, time is running out."
            print(reminder)
        elif time_bound == "no":
            reminder = f"'{task}' is a {priority} priority task. But you can complete it in your free time."
            print(reminder)
    case "low":
        if time_bound == "yes":
            reminder = f"'{task}' is a {priority} priority task. Time is running out!"
            print(reminder)
        elif time_bound == "no":
            reminder = f"'{task}' is a {priority} priority task. Consider completing it in your free time."
            print(reminder)
    case _:
        reminder = f"incorrect input!"
        print(reminder)
