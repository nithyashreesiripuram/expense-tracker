import json
import os
from datetime import datetime
class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()
    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []
    def save_expenses(self):
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=4)
    def add_expense(self, amount, category, description):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be positive.")
        except ValueError as e:
            print(f"Invalid amount: {e}")
            return
        expense = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "amount": amount,
            "category": category,
            "description": description
        }
        self.expenses.append(expense)
        self.save_expenses()
        print("Expense added successfully!")
    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        print("\nExpense History:")
        for exp in self.expenses:
            print(f"{exp['date']} - {exp['category']}: ${exp['amount']} ({exp['description']})")
    def get_monthly_summary(self):
        monthly_summary = {}
        for exp in self.expenses:
            month = exp['date'][:7]
            monthly_summary[month] = monthly_summary.get(month, 0) + exp['amount']
        print("\nMonthly Summary:")
        for month, total in monthly_summary.items():
            print(f"{month}: ${total:.2f}")
    def get_category_summary(self):
        category_summary = {}
        for exp in self.expenses:
            category = exp['category']
            category_summary[category] = category_summary.get(category, 0) + exp['amount']
        print("\nCategory-wise Summary:")
        for category, total in category_summary.items():
            print(f"{category}: ${total:.2f}")
    def run(self):
        while True:
            print("\nExpense Tracker Menu:")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Monthly Summary")
            print("4. Category Summary")
            print("5. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                amount = input("Enter amount: ")
                category = input("Enter category: ")
                description = input("Enter description: ")
                self.add_expense(amount, category, description)
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.get_monthly_summary()
            elif choice == '4':
                self.get_category_summary()
            elif choice == '5':
                print("Exiting Expense Tracker. Have a great day!")
                break
            else:
                print("Invalid option. Please try again.")
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()