def bank(x, y):
    n = 0.10
    s = x * (1 + n) ** y
    s1 = round(s, 2)
    return s1
x = int(input("Начальная сумма вклада: "))
y = int(input("Количество лет: "))

s = bank(x, y)
print(f"Сумма на счету через {y} лет составит: {s}")