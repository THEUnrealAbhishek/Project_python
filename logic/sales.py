import csv
import os

PRODUCTS_FILE = "data/products.csv"
SALES_FILE = "data/sales.csv"


def ensure_sales_file():
    if not os.path.isfile(SALES_FILE):
        with open(SALES_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["product", "price", "quantity", "total"])


def sell_product(product_name, qty_sold):
    """
    Handles billing:
    - checks stock
    - reduces product quantity
    - saves sale
    """
    if qty_sold <= 0:
        return False, "Invalid quantity"

    # read products
    with open(PRODUCTS_FILE, newline="") as f:
        products = list(csv.DictReader(f))

    updated_products = []
    sale_done = False
    message = ""

    for p in products:
        stock = int(p["quantity"])

        if p["name"] == product_name:
            if qty_sold > stock:
                message = "Not enough stock available"
            else:
                price = float(p["price"])
                total = price * qty_sold
                p["quantity"] = stock - qty_sold

                ensure_sales_file()
                with open(SALES_FILE, "a", newline="") as sf:
                    writer = csv.writer(sf)
                    writer.writerow([product_name, price, qty_sold, total])

                sale_done = True
                message = "Bill generated successfully"

        updated_products.append(p)

    # update products file if sale succeeded
    if sale_done:
        with open(PRODUCTS_FILE, "w", newline="") as f:
            writer = csv.DictWriter(
                f, fieldnames=["name", "price", "quantity"]
            )
            writer.writeheader()
            writer.writerows(updated_products)

        return True, message

    return False, message
