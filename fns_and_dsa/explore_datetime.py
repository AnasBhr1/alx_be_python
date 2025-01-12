from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS.
    """
    current_date = datetime.now()  # Get current date and time
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    """
    Calculates a future date by adding the specified number of days to the current date.
    """
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=days_to_add)  # Calculate future date
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

def main():
    """
    Main function to display the current datetime and calculate a future date.
    """
    display_current_datetime()  # Show current date and time
    calculate_future_date()  # Ask user for days and display future date

if __name__ == "__main__":
    main()  # Run the main function
