def process_order(order):
    if "customer" not in order:
        raise Exception("Customer missing")

    if "items" not in order:
        raise Exception("Items missing")

    subtotal = 0

    for item in order["items"]:
        if item["price"] < 0:
            raise Exception("Negative price")

        if item["quantity"] <= 0:
            raise Exception("Invalid quantity")

        subtotal += item["price"] * item["quantity"]

    discount = 0

    if subtotal >= 5000:
        discount = subtotal * 0.20
    elif subtotal >= 2000:
        discount = subtotal * 0.10

    taxable = subtotal - discount
    tax = taxable * 0.18
    total = taxable + tax

    invoice = {
        "customer": order["customer"],
        "subtotal": round(subtotal, 2),
        "discount": round(discount, 2),
        "tax": round(tax, 2),
        "total": round(total, 2),
    }

    print("=" * 30)
    print("Invoice")
    print("=" * 30)
    print("Customer:", invoice["customer"])
    print("Subtotal:", invoice["subtotal"])
    print("Discount:", invoice["discount"])
    print("Tax:", invoice["tax"])
    print("Total:", invoice["total"])

    return invoice