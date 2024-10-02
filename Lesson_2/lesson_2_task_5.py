def month_to_season(n):
        if n >= 1 and n <= 2 or n == 12:
            return("Winter")
        elif n >= 3 and n <= 5:
            return("Spring")
        elif n >= 6 and n <= 8:
            return("Summer")
        elif n >= 9 and n <= 11:
            return("Autumn")
        else:
            return("out of range")

n = int(input("Month num: "))
result = month_to_season(n)
print(result)