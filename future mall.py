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

    # Sample customer cart
    sample_cart = {"Meat": 1, "Cheese": 2, "Milk": 1}
    
    print("\n--- YOUR RECEIPT ---")
    for item, qty in sample_cart.items():
        if item in products:
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