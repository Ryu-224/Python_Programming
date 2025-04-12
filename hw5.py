def read_single_digit(n):
    
    korean = {0: "공", 1: "하나", 2: "둘", 3: "삼", 4: "넷", 5: "오", 6: "여섯", 7: "칠", 8: "팔", 9: "아홉"}
    
    return korean[n]

def read_number(num):
    if num < 10:
        return read_single_digit(num)
    
    elif num < 100:
        ten = num // 10
        one = num % 10
        return f"{read_single_digit(ten)} {read_single_digit(one)}"
    
    elif num < 1000:
        hundred = num // 100
        ten = (num // 10) % 10
        one = num % 10
        return f"{read_single_digit(hundred)} {read_single_digit(ten)} {read_single_digit(one)}"
    
    else:
        return "오류"

number = int(input("세 자리 정수 입력: "))
print(read_number(number))