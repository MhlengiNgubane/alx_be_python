import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date():
    try:
        num_days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.datetime.now()
        future_date = current_date + datetime.timedelta(days=number_of_days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future Date after {number_of_days} days: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter a valid integer number of days.")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()