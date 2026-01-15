product_prices = (1200, 850, 430, 999)

print("Product Prices:", product_prices)
print("\nTrying to modify price...")
try:
    product_prices[1] = 900   
except TypeError as e:
    print("Error:", e)
    print("Tuple values cannot be modified (immutable).")
print("\nAccessing using index:")
print("First product price:", product_prices[0])
print("Last product price:", product_prices[-1])
print("\nWhy Tuple?")
print("Tuple is used because product prices are fixed and should not be changed.")
