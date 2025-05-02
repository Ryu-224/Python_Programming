showpping_bag = {}
print("[구입]")

while True:
    item = input("상품명? ")
    if item == "":
        break
    amount = int(input("수량은? "))
    showpping_bag[item] = amount
    print(f"장바구니에 {item} {amount}개가 담겼습니다.\n")

print(f"\n>>> 장바구니 보기: {showpping_bag}")

print("\n[검색]")
find = input("장바구니에서 확인하고자 하는 상품은? ")
if find in showpping_bag:
    print(f"{find}은(는) {showpping_bag.get(find)}개 담겨 있습니다.")
else:
    print(f"{find}은(는) 장바구니에 없습니다.")