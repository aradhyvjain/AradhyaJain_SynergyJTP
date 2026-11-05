"""
Expense Tracker - a small project practising core Python concepts:
  - variables & data types (str, float, int, list, dict, tuple, bool)
  - loops (while for the menu, for to iterate expenses)
  - conditions (if / elif / else)
  - functions (small, single-purpose)
  - file handling (reading/writing a CSV file)
  - error handling (try / except / finally)
 
Run it with:  python expense_tracker.py
"""
 
import csv
from datetime import date
 
FILE_NAME = "expenses.csv"          # str constant
CATEGORIES = ("Food", "Transport", "Bills", "Shopping", "Other")  # tuple
 
 
# ---------- File handling ----------
 
def load_expenses(filename=FILE_NAME):
    """Read expenses from a CSV file and return a list of dicts."""
    expenses = []
    try:
        with open(filename, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    expenses.append({
                        "date": row["date"],
                        "category": row["category"],
                        "description": row["description"],
                        "amount": float(row["amount"]),
                    })
                except (KeyError, ValueError):
                    print(f"  Skipping a corrupted row: {row}")
    except FileNotFoundError:
        print("No saved file found - starting fresh.")
    return expenses
 
 
def save_expenses(expenses, filename=FILE_NAME):
    """Write the list of expenses to a CSV file."""
    try:
        with open(filename, "w", newline="") as f:
            fields = ["date", "category", "description", "amount"]
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(expenses)
        print(f"Saved {len(expenses)} expense(s) to {filename}.")
    except OSError as error:
        print(f"Could not save file: {error}")
 
 
# ---------- Input helpers (error handling) ----------
 
def get_amount(prompt="Amount: "):
    """Keep asking until the user enters a valid positive number."""
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("  Amount must be greater than zero.")
            else:
                return round(amount, 2)
        except ValueError:
            print("  Please enter a number, e.g. 12.50")
 
 
def get_category():
    """Show numbered categories and return the chosen one."""
    for number, name in enumerate(CATEGORIES, start=1):
        print(f"  {number}. {name}")
    while True:
        choice = input("Choose category number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        print("  Invalid choice, try again.")
 
 
# ---------- Core features ----------
 
def add_expense(expenses):
    description = input("Description: ").strip() or "No description"
    category = get_category()
    amount = get_amount()
    expenses.append({
        "date": str(date.today()),
        "category": category,
        "description": description,
        "amount": amount,
    })
    print(f"Added: {description} - {amount:.2f} ({category})")
 
 
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print(f"\n{'#':<4}{'Date':<12}{'Category':<11}{'Description':<20}{'Amount':>9}")
    print("-" * 56)
    for index, e in enumerate(expenses, start=1):
        print(f"{index:<4}{e['date']:<12}{e['category']:<11}"
              f"{e['description'][:19]:<20}{e['amount']:>9.2f}")
 
 
def total_spent(expenses):
    total = 0.0
    for e in expenses:
        total += e["amount"]
    return total
 
 
def summary_by_category(expenses):
    """Build a dict of category -> total and print it with percentages."""
    if not expenses:
        print("Nothing to summarise yet.")
        return
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
 
    grand_total = total_spent(expenses)
    print("\n--- Spending Summary ---")
    for category, amount in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        percent = amount / grand_total * 100
        bar = "#" * int(percent // 5)
        print(f"{category:<10}{amount:>9.2f}  {percent:5.1f}%  {bar}")
    print("-" * 30)
    print(f"{'TOTAL':<10}{grand_total:>9.2f}")
 
    top = max(totals, key=totals.get)
    print(f"Biggest spending area: {top}")
 
 
def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    try:
        number = int(input("Number to delete (0 to cancel): "))
        if number == 0:
            return
        removed = expenses.pop(number - 1)
        print(f"Deleted: {removed['description']}")
    except ValueError:
        print("Please enter a valid number.")
    except IndexError:
        print("No expense with that number.")
 
 
def check_budget(expenses):
    limit = get_amount("Enter your budget: ")
    spent = total_spent(expenses)
    remaining = limit - spent
    if remaining < 0:
        print(f"Over budget by {abs(remaining):.2f}!")
    elif remaining < limit * 0.2:
        print(f"Careful - only {remaining:.2f} left ({spent:.2f} spent).")
    else:
        print(f"You're on track. {remaining:.2f} left ({spent:.2f} spent).")
 
 
# ---------- Main program loop ----------
 
def main():
    expenses = load_expenses()
    menu = (
        "\n=== Expense Tracker ===\n"
        "1. Add expense\n"
        "2. View expenses\n"
        "3. Summary by category\n"
        "4. Check budget\n"
        "5. Delete expense\n"
        "6. Save & quit\n"
    )
    running = True
    while running:
        print(menu)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            summary_by_category(expenses)
        elif choice == "4":
            check_budget(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            save_expenses(expenses)
            running = False
        else:
            print("Invalid option, please pick 1-6.")
    print("Goodbye!")
 
 
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nExited without saving.")