# file: discount_calculator.py

def calculate_discount(price: float, discount_rate: float) -> float:
    """Return the final price after applying the discount if >=20% else return original price."""
    if discount_rate >= 20:
        discount_amount = (discount_rate / 100) * price
        return price - discount_amount
    return price

if __name__ == "__main__":
    try:
        # Get user inputs
        original_price = float(input("Enter the original price: "))
        discount_percent = float(input("Enter the discount percentage: "))

        final_price = calculate_discount(original_price, discount_percent)

        if final_price < original_price:
            print(f"Discount applied! Final price is: ${final_price:.2f}")
        else:
            print(f"No discount applied. Final price remains: ${final_price:.2f}")

    except ValueError:
        print("Please enter valid numbers for price and discount.")