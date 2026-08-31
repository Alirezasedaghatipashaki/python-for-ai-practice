def chai_bill(cups, *addons, **discount):
    # Calculate base price for chai
    chai_price = cups * 15
    
    # Calculate price for additional items
    addons_price = len(addons) * 5
    
    # Total cost before discount
    total = chai_price + addons_price
    
    # Apply discount if specified
    if "discount_percent" in discount:
        percent = discount["discount_percent"]
        total = total - (total * percent / 100)
        
    return total


# Test cases
print(chai_bill(2))
print(chai_bill(3, "ginger", "masala"))
print(chai_bill(4, "biscuit", discount_percent=10))
print(chai_bill(5, "ginger", "masala", "biscuit", discount_percent=20))
