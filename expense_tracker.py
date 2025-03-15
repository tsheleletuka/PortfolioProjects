import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

#file to store expenses
EXPENSES_FILE = "expenses.csv"

# Initialize the csv file if it does not exist
def initialize_file():
    try:
        with open(EXPENSES_FILE, "x", newline= "") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])
    except FileExistsError:
        pass

# add an expense
def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Rent, Entertainment): ")
    description = input("Enter a description: ")
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    with open(EXPENSES_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print("Expense added successfully!")

# View expenses
def view_expenses():
    try:
        df = pd.read_csv(EXPENSES_FILE)
        print("\nExpenses:\n")
        print(df.to_string(index=False))
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Analyze spending
def analyze_spending():
    try:
        df = pd.read_csv(EXPENSES_FILE)
        if df.empty:
            print("No expenseses recorded yet.")
            return

        # Ensure "Amount" column is numeric
        df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
        df.dropna(subset=["Amount"], inplace=True)  # Drop rows with invalid amounts

        # calculate total spending
        total = df["Amount"].sum()
        print(f"\nTotal Spending: {total:.2f}\n")


        # show spending by category
        category_summary = df.groupby("Category")["Amount"].sum()
        print("Spending by Category: ")
        print(category_summary)

        # Pie Chart
        category_summary.plot(kind="pie", autopct="%1.1f%%", title="Spending Breakdown by Category")
        plt.ylabel("") # Remove the default y-axis label
        plt.show()
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Export data
def export_data():
    try:
        df = pd.read_csv(EXPENSES_FILE)
        if df.empty:
            print("No expense to export.")
            return

        output_file = input("Enter the name of the output file (e.g., export.csv): ")
        df.to_csv(output_file, index=False)
        print(f"Expenses export to {output_file} successfully!")
    except FileNotFoundError:
        print("No expenses recorded yet.")

def main():
    initialize_file()

    while True:
        print("\n")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Spending")
        print("4. Export Data")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            analyze_spending()
        elif choice == "4":
            export_data()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
