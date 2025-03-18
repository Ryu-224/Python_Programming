def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(r2):
    area = 3.14 * r2 * r2
    return area

r2 = get_radius("넓이를 구하고자 하는 원의 반지름은? ")
area = get_circle_area(r2)
print("반지름 %d인 원의 넓이 = 3.14 x %d x %d = %.2f" % (r2, r2, r2, area))