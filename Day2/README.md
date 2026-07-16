# Production Refactoring Exercise

## Overview

This exercise demonstrates how to refactor a large, difficult-to-maintain function into a collection of small, focused, and reusable functions that follow production-level Python coding standards.

The original implementation contains all business logic inside a single function. The refactored version applies clean code principles such as the **Single Responsibility Principle (SRP)**, **type hints**, **documentation**, and **modularity**.

---

## Objectives

- Break a large function into smaller functions.
- Add Python type hints.
- Write descriptive docstrings.
- Improve readability and maintainability.
- Produce code that resembles a real production codebase.

---

## Original Problem

The initial implementation performs multiple responsibilities inside one function:

- Validates the order
- Calculates subtotal
- Applies discounts
- Calculates tax
- Builds the invoice
- Prints the invoice

This makes the function:

- Hard to read
- Difficult to test
- Difficult to extend
- Difficult to debug

---

## Refactoring Strategy

The large function is divided into the following smaller functions:

| Function | Responsibility |
|----------|----------------|
| `validate_order()` | Validates input data |
| `calculate_subtotal()` | Computes subtotal |
| `calculate_discount()` | Determines applicable discount |
| `calculate_tax()` | Calculates tax |
| `build_invoice()` | Creates the invoice dictionary |
| `print_invoice()` | Displays the invoice |
| `process_order()` | Coordinates the complete workflow |

Each function has one well-defined responsibility.

---

## Features

- ✅ Production-style code organization
- ✅ Complete type hints
- ✅ Comprehensive docstrings
- ✅ Easy to test
- ✅ Easy to maintain
- ✅ Easy to extend

---

## Example Input

```python
order = {
    "customer": "Naren",
    "items": [
        {"price": 500, "quantity": 2},
        {"price": 1500, "quantity": 3},
    ],
}

invoice = process_order(order)
```

---

## Example Output

```text
==============================
INVOICE
==============================
Customer : Naren
Subtotal : 5500
Discount : 1100.0
Tax      : 792.0
Total    : 5192.0
```

---

## Running the Project

Run the application using Python:

```bash
python order_processor.py
```

---

## Production Practices Demonstrated

This project demonstrates the following software engineering principles:

- **Single Responsibility Principle (SRP)**
- **Modular Design**
- **Type Hints**
- **Function Documentation (Docstrings)**
- **Named Constants**
- **Separation of Concerns**
- **Readable Code Formatting**
- **Maintainable Project Structure**
- **Production-Ready Code Organization**

---

## Learning Outcomes

- Refactor large functions into smaller reusable functions
- Apply clean code principles
- Write production-quality Python code
- Use type hints effectively
- Document code with docstrings
- Organize code for readability and maintainability

---