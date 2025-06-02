# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Enter the priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Start processing based on priority using match-case (Python 3.10+)
match priority:
    case "high":
        reminder = f"🔴 High Priority Task: '{task}'."
    case "medium":
        reminder = f"🟠 Medium Priority Task: '{task}'."
    case "low":
        reminder = f"🟢 Low Priority Task: '{task}'."
    case _:
        reminder = f"⚪ Task: '{task}' (Unknown priority level)."

# Modify the message if the task is time-bound
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Print the final reminder
print("\n" + reminder)
