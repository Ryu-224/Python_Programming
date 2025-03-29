def get_fixed_price(price):
    fixed_price = 100 * price / (100 - rate)
    return int(fixed_price)


rate = int(input("할인율은? "))
A = int(input("A 상품의 할인된 가격은? "))
B = int(input("B 상품의 할인된 가격은? "))
print("A 상품의 정가는", get_fixed_price(A), "원")
print("B 상품의 정가는", get_fixed_price(B), "원")