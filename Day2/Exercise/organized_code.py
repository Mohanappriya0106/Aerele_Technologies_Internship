from typing import Any

TAX_RATE = 0.18
HIGH_DISCOUNT_THRESHOLD = 5000
MEDIUM_DISCOUNT_THRESHOLD = 2000
HIGH_DISCOUNT_RATE = 0.20
MEDIUM_DISCOUNT_RATE = 0.10

def validate_order(order: dict[str, Any]) -> None:
    """
        Validate the structure and contents of an order.
        Raises ValueError if required fields are missing or item values are invalid.
    """
    
    if "customer" not in order:
        raise ValueError("Customer is required.")

    if "items" not in order:
        raise ValueError("Items are required.")

    for item in order["items"]:
        if item["price"] < 0:
            raise ValueError("Price cannot be negative.")

        if item["quantity"] <= 0:
            raise ValueError("Quantity must be greater than zero.")

def calculate_subtotal(items: list[dict[str, Any]]) -> float:
    """
        Calculate the subtotal for all items.Total price before discounts and tax.
    """
    return sum(item["price"] * item["quantity"] for item in items)

def calculate_discount(subtotal: float) -> float:
    """
        Calculate discount based on subtotal.
        Returns Discount amount.
    """
    if subtotal >= HIGH_DISCOUNT_THRESHOLD:
        return subtotal * HIGH_DISCOUNT_RATE

    if subtotal >= MEDIUM_DISCOUNT_THRESHOLD:
        return subtotal * MEDIUM_DISCOUNT_RATE

    return 0.0

def calculate_tax(amount: float) -> float:
    """
        Calculate GST on the taxable amount.
        Returns Tax amount.
    """
    return amount * TAX_RATE

def build_invoice(customer: str,subtotal: float,discount: float,tax: float) -> dict[str, float | str]:
    """
        Construct the invoice dictionary.
        Returns Final invoice.
    """
    total = subtotal - discount + tax

    return {
        "customer": customer,
        "subtotal": round(subtotal, 2),
        "discount": round(discount, 2),
        "tax": round(tax, 2),
        "total": round(total, 2),
    }

def print_invoice(invoice: dict[str, float | str]) -> None:
    """
        Display the invoice in a readable format.
    """
    print("=" * 30)
    print("INVOICE")
    print("=" * 30)

    print(f"Customer : {invoice['customer']}")
    print(f"Subtotal : {invoice['subtotal']}")
    print(f"Discount : {invoice['discount']}")
    print(f"Tax      : {invoice['tax']}")
    print(f"Total    : {invoice['total']}")

def process_order(order: dict[str, Any]) -> dict[str, float | str]:
    """
        Process an order from validation through invoice generation.
        Returns Final invoice.
    """
    validate_order(order)

    subtotal = calculate_subtotal(order["items"])
    discount = calculate_discount(subtotal)

    taxable_amount = subtotal - discount
    tax = calculate_tax(taxable_amount)

    invoice = build_invoice(
        customer=order["customer"],
        subtotal=subtotal,
        discount=discount,
        tax=tax,
    )

    print_invoice(invoice)

    return invoice

