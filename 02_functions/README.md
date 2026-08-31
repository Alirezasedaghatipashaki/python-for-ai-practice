# Exercise 2: Chai Stall Bill Calculator

## Problem Statement
You run a chai stall. Customers order multiple cups of chai, sometimes with add-ons (extra ginger, masala, biscuits). Write a function `chai_bill(cups, *addons, **discount)` to calculate their bill.

### Requirements
- Charges ₹15 per cup of chai.
- Adds ₹5 for each addon passed via `*args` (e.g., "ginger", "masala", "biscuit").
- Applies a discount only if `discount_percent` is passed via `**kwargs`.
- Returns the final bill amount.

### Test Cases & Expected Output
print(chai_bill(2))
# Expected Output: 30

print(chai_bill(3, "ginger", "masala"))
# Expected Output: 55

print(chai_bill(4, "biscuit", discount_percent=10))
# Expected Output: 58.5

print(chai_bill(5, "ginger", "masala", "biscuit", discount_percent=20))
# Expected Output: 112.0
