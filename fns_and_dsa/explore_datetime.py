from datetime import date, datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time is : {formatted}")

def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    today = date.today()
    future_date = today + timedelta(days=days)
    print(f"Future date: {future_date}")

display_current_datetime()
calculate_future_date()

