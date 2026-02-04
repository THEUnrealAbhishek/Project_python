import csv
import os

SALES_FILE = "data/sales.csv"
EXPENSES_FILE = "data/expenses.csv"


def ensure_sales_file():
    if not os.path.isfile(SALES_FILE):
        with open(SALES_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["product", "price", "quantity", "total"])


def ensure_expenses_file():
    if not os.path.isfile(EXPENSES_FILE):
        with open(EXPENSES_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["title", "amount"])


def get_total_sales():
    """
    Returns total sales amount
    """
    ensure_sales_file()
    total = 0

    with open(SALES_FILE, newline="") as f:
        for row in csv.DictReader(f):
            total += float(row["total"])

    return total


def get_total_expenses():
    """
    Returns total expenses amount
    """
    ensure_expenses_file()
    total = 0

    with open(EXPENSES_FILE, newline="") as f:
        for row in csv.DictReader(f):
            total += float(row["amount"])

    return total


def get_profit():
    """
    Returns profit or loss
    """
    return get_total_sales() - get_total_expenses()
