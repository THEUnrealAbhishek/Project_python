import csv
import os

PRODUCTS_FILE = "data/products.csv"


def ensure_products_file():
    if not os.path.isfile(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "price", "quantity"])


def add_product(name, price, quantity):
    ensure_products_file()

    if price <= 0 or quantity <= 0:
        return False, "Invalid product data"

    with open(PRODUCTS_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, price, quantity])

    return True, "Product added successfully"


def get_all_products():
    ensure_products_file()

    with open(PRODUCTS_FILE, newline="") as f:
        return list(csv.DictReader(f))


def update_products(products):
    with open(PRODUCTS_FILE, "w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["name", "price", "quantity"]
        )
        writer.writeheader()
        writer.writerows(products)
