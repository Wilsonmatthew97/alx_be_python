from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("current date and time: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    num_of_days = int(input("Enter the number of days to add to the current date: "))
    def calculate_future_date():
        future_date = current_date + timedelta(days=num_of_days)
        print("Future date: ", future_date.strftime("%Y-%m-%d"))
    calculate_future_date()
display_current_datetime()
