from datetime import datetime, timedelta

def display_current_datetime():
    # Save the current date and time
    current_date = datetime.now()

    # Format date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Print the formatted date and time
    print("Current Date and Time:", formatted_date)


# Call the function
display_current_datetime()


# Function to calculate future date
def calculate_future_date(days):
    # Get today's date
    current_date = datetime.now()

    # Add the number of days
    future_date = current_date + timedelta(days=days)

    # Format the future date
    formatted_future = future_date.strftime("%Y-%m-%d")

    # Print result
    print("The future date is:", formatted_future)


# --- Main Program ---
# Prompt the user
days_input = int(input("Enter the number of days to add to the current date: "))

# Call the function
calculate_future_date(days_input)