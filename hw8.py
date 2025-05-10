def buy(dic):
    print("[구입]")
    item = input("상품명? ")
    if item == "":
        return False
    amount = int(input("수량은? "))
    dic[item] = amount
    print(f"장바구니에 {item} {amount}개가 담겼습니다.\n")

def show(dic):
    print(f"\n>>> 장바구니 보기: {dic}")

def find(dic):
    print("\n[검색]")
    item = input("장바구니에서 확인하고자 하는 상품은? ")
    if item in dic:
        print(f"{item}은(는) {dic.get(item)}개 담겨 있습니다.")
    else:
        print(f"장바구니에 {item}은(는) 없습니다.")

showpping_bag = {}
while True:
    if buy(showpping_bag) == False:
        break
show(showpping_bag)
find(showpping_bag)