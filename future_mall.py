import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# ===================================================
# Task 1: Cashier System Setup
# ===================================================
MALL_NAME = "future Mall"

# Product items and prices
products = {
    "Milk": 35,
    "Bread": 15,
    "Cheese": 80,
    "Meat": 380,
    "Juice": 25
}

def run_cashier_system():
    print(f"\n" + "="*40)
    print(f"       WELCOME TO {MALL_NAME.upper()}")
    print("="*40)
    
    total_price = 0.0

    # Display available products
    print("\nAvailable Products:")
    for item, price in products.items():
        print(f" - {item}: {price} EGP")
    print("-" * 40)

    # Dynamic Customer Cart
    cart = {}
    print("\nEnter products to purchase (type 'done' to finish):")
    
    while True:
        item_input = input("Enter product name: ").strip().capitalize()
        
        if item_input.lower() == 'done':
            break
            
        if item_input in products:
            try:
                qty = int(input(f"Enter quantity for {item_input}: "))
                if qty <= 0:
                    print("Quantity must be greater than 0.")
                    continue
                # Update quantity if product is already in cart
                cart[item_input] = cart.get(item_input, 0) + qty
                print(f"--> Added {qty} x {item_input} to cart.")
            except ValueError:
                print("Invalid quantity! Please enter a valid number.")
        else:
            print("Product not found! Please choose from the list above.")
        print("-" * 20)

    # Check if cart is empty
    if not cart:
        print("\nNo items selected. Thank you for visiting!")
        print("=" * 40 + "\n")
        return

    # Print Receipt
    print("\n--- YOUR RECEIPT ---")
    for item, qty in cart.items():
        item_total = products[item] * qty
        total_price += item_total
        print(f"{item} x{qty} : {item_total} EGP")
            
    print("-" * 40)
    print(f"Subtotal: {total_price:.2f} EGP")

    # Discount Rule: 10% discount for orders equal to or exceeding 500 EGP
    if total_price >= 500:
        discount = total_price * 0.10
        final_price = total_price - discount
        print(f"Discount (10% applied for >= 500 EGP): -{discount:.2f} EGP")
        print(f"TOTAL AMOUNT: {final_price:.2f} EGP")
    else:
        print("Discount: 0.00 EGP (Spend 500 EGP or more to get 10% off!)")
        print(f"TOTAL AMOUNT: {total_price:.2f} EGP")
        
    print("=" * 40 + "\n")

if __name__ == "__main__":
    run_cashier_system()