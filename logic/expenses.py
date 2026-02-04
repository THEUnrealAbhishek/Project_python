import csv
import os

EXPENSES_FILE = "data/expenses.csv"


def ensure_expenses_file():
    if not os.path.isfile(EXPENSES_FILE):
        with open(EXPENSES_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["title", "amount"])


def add_expense(title, amount):
    """
    Adds a new expense entry after validation
    """
    ensure_expenses_file()

    if amount <= 0:
        return False, "Invalid expense amount"

    with open(EXPENSES_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([title, amount])

    return True, "Expense added successfully"


def get_all_expenses():
    """
    Returns list of all expenses
    """
    ensure_expenses_file()

    with open(EXPENSES_FILE, newline="") as f:
        return list(csv.DictReader(f))
