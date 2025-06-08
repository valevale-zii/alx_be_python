# File: explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Returns the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date

def calculate_future_date(days):
    """
    Returns the future date after adding 'days' to current date in 'YYYY-MM-DD' format.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    return formatted_future_date

# Main execution
if __name__ == "__main__":
    # Display current date and time
    current_datetime = display_current_datetime()
    print(f"Current date and time: {current_datetime}")

    try:
        # Get user input and calculate future date
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = calculate_future_date(days_to_add)
        print(f"Future date: {future_date}")
    except ValueError:
        print("Please enter a valid integer number of days.")
