from flask import Flask, render_template, request, redirect, url_for

# ---------------- LOGIC IMPORTS ----------------
from logic.products import add_product, get_all_products
from logic.sales import sell_product
from logic.expenses import add_expense, get_all_expenses
from logic.analytics import get_total_sales, get_total_expenses, get_profit

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route("/")
def index():
    return render_template("index.html")


# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    # Demo login (authentication not implemented)
    if request.method == "POST":
        return redirect(url_for("dashboard"))
    return render_template("login.html")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ---------------- PRODUCTS ----------------
@app.route("/products", methods=["GET", "POST"])
def products():
    message = None

    if request.method == "POST":
        success, message = add_product(
            request.form["name"].strip(),
            float(request.form["price"]),
            int(request.form["quantity"])
        )

    products_list = get_all_products()

    return render_template(
        "products.html",
        products=products_list,
        message=message
    )


# ---------------- BILLING ----------------
@app.route("/billing", methods=["GET", "POST"])
def billing():
    message = None
    products_list = get_all_products()

    if request.method == "POST":
        success, message = sell_product(
            request.form["product"],
            int(request.form["quantity"])
        )

    return render_template(
        "billing.html",
        products=products_list,
        message=message
    )


# ---------------- EXPENSES ----------------
@app.route("/expenses", methods=["GET", "POST"])
def expenses():
    message = None

    if request.method == "POST":
        success, message = add_expense(
            request.form["title"].strip(),
            float(request.form["amount"])
        )

    expenses_list = get_all_expenses()

    return render_template(
        "expenses.html",
        expenses=expenses_list,
        message=message
    )


# ---------------- REPORTS ----------------
@app.route("/reports")
def reports():
    return render_template(
        "reports.html",
        total_sales=get_total_sales(),
        total_expenses=get_total_expenses(),
        profit=get_profit()
    )


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)