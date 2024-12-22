# daily_reminder.py
# A script to remind the user about a task based on priority and time sensitivity.

# Prompt the user for the task description
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").strip().lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Default message to print
reminder_message = ""

# Use a match case statement to handle the task based on priority
match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task"
    case "medium":
        reminder_message = f"'{task}' is a medium priority task"
    case "low":
        reminder_message = f"'{task}' is a low priority task"
    case _:
        reminder_message = "Invalid priority. Please choose from high, medium, or low."

# Check if the task is time-bound and modify the reminder accordingly
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"
elif time_bound == "no":
    reminder_message += ". Consider completing it when you have free time."

# Print the reminder message
print("Reminder:", reminder_message)
