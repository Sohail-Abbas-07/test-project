def add_all(*nums: int) -> int:
    return sum(nums)


def apply_discount(price: int, discount_rate: float = 0.10) -> float:
    # Applies a default 10% discount
    return price * (1 - discount_rate)


def calculate_tax(amount: float, tax_rate: float = 0.08) -> float:
    # Applies a default 8% tax
    return amount * (1 + tax_rate)


def checkout(*nums: int) -> float:
    print(*nums)
    total_price = add_all(*nums)

    gross_total = apply_discount(total_price)

    net_total = calculate_tax(gross_total)

    return net_total


final_amount = checkout(100, 250, 50)
print(f"Final Net Total: {final_amount:.2f}")
