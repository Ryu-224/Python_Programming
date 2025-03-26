def exchange(price):
    n = price

    n500 = n // 500
    n %= 500

    n100 = n // 100
    n %= 100

    n50 = n // 50
    n %= 50

    n10 = n // 10
    print("500원 동전의 개수: ",n500,"\n""100원 동전의 개수: ",n100,"\n""50원 동전의 개수: ",n50,"\n""10원 동전의 개수: ",n10)

def get_integer(prompt):
    res = int(input(prompt))
    return res

price = get_integer("동전으로 교환하고자 하는 금액은? ")
exchange(price)
