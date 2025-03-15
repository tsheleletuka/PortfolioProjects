import json
import os
from datetime import date

# File to store habits data

DATA_FILE = "habit_tracker.json"

# Load habits data from file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

# Save habits data to a file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add a new habit
def add_habit(habits):
    name = input("Enter the habit name: ")
    if name in habits:
        print("Habit already exists!")
        return
    habits[name] = {"streak": 0, "last_completed": None}
    print(f"Habit '{name}' added!")


# Mark a habit as complete
def complete_habit(habits):
    name = input("Enter the habit name: ")
    if name not in habits:
        print("Habit not found!")
        return
    today = str(date.today())
    if habits[name]["last_completed"] == today:
        print(f"You've already marked '{name} as complete today!")
    else:
        habits[name]["streak"] += 1
        habits[name]["last_completed"] = today
        print(f"Habit '{name} marked as completed! Current streak: {habits[name]['streak']}")

# View all habits and their progress
def view_habits(habits):
    if not habits:
        print("No habits to display. Add some first!")
        return
    print("\nYour Habits:")
    for name, details in habits.items():
        print(f"- {name}: Streak {details['streak']} (Last copleted: {details['last_completed']})")


def delete_habit(habits):
    name = input("Enter the habit name to delete: ")
    if name in habits:
        del habits[name]
        print(f"Habit '{name} deleted.")
    else:
        print("Habit not found!")

# Main menu
def main():
    habits = load_data()
    while True:
        print("\n--- Habit Tracker ---")
        print("1. Add Habit")
        print("2. Mark Habit as Complete")
        print("3. View Habits")
        print("4. Delete Habit")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            complete_habit(habits)
        elif choice == "3":
            view_habits(habits)
        elif choice == "4":
            delete_habit(habits)
        elif choice == "5":
            save_data(habits)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()