# To-Do List Manager

# Function to display the main menu options to the user
def show_menu():
    print("\nTo-Do List Manager")
    print("1. View To-Do List")  # Option to view the current to-do list
    print("2. Add a Task")       # Option to add a new task
    print("3. Remove a Task")    # Option to remove an existing task
    print("4. Exit")             # Option to exit the program

# Function to display all tasks in the to-do list
def view_tasks(tasks):
    # Check if the list is empty
    if not tasks:
        print("\nYour to-do list is empty")  # Notify user if no tasks are present
    else:
        print("\nYour To-Do List:")  # Display all tasks with numbers
        for i, task in enumerate(tasks, start=1):  # Enumerate assigns a number to each task
            print(f"{i}. {task}")

# Function to add a new task to the to-do list
def add_task(tasks):
    # Prompt the user to enter a new task
    task = input("\nEnter the task you want to add: ").strip()

    # Add the task to the list if it's not empty
    if task:
        tasks.append(task)
        print(f'"{task}" has been added to your to-do list.')  # Confirmation message
    else:
        print("Task cannot be empty.")  # Notify user that an empty task is invalid

# Function to remove a task from the to-do list
def remove_task(tasks):
    # Display the current tasks to the user for reference
    view_tasks(tasks)

    # Proceed only if the list is not empty
    if tasks:
        try:
            # Prompt the user to enter the task number they want to remove
            task_number = int(input("\nEnter the number of the task to remove: "))
            
            # Check if the entered number is valid
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)  # Remove the task from the list
                print(f'"{removed_task}" has been removed from your to-do list.')  # Confirmation message
            else:
                print("Invalid task number")  # Notify user if number is out of range
        except ValueError:
            print("Please enter a valid number.")  # Handle invalid input (non-integer)

# Main function to run the program
def main():
    # Initialize an empty list to store tasks
    tasks = []

    # Run the program in a continuous loop
    while True:
        # Display the menu options
        show_menu()

        # Prompt the user to choose an option
        choice = input("\nChoose an option (1 - 4): ").strip()

        # Handle user choice
        if choice == '1':
            view_tasks(tasks)  # View the list of tasks
        elif choice == '2':
            add_task(tasks)  # Add a new task
        elif choice == '3':
            remove_task(tasks)  # Remove an existing task
        elif choice == '4':
            print("Exiting the To-Do List Manager. Goodbye!")  # Exit the program
            break  # Break the loop to end the program
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")  # Handle invalid input

# Entry point of the program
if __name__ == "__main__":
    main()
