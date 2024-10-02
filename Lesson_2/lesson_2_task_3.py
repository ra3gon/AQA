
def square(x):
    area = x * x
    if area == int(area):
        return int(area)
    else:
        return int(area) + 1
x = 2.2
area = square(x)
print("area = ", area)
