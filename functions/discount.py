def calculate_discounted_price(price, discount):
    discounted = price * discount / 100
    final_price = price - discounted
    return final_price

if __name__ == "__main__":
    # Phone 
    price = 30000
    discount = 10
    discounted_price = calculate_discounted_price(price, discount)
    print(f"The discounted price of {price} with a discount of {discount}% is: {discounted_price}")