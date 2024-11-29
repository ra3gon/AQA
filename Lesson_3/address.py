class Address:
    def __init__(self, index, city, street, build, apart):
        self.index = index
        self.city = city
        self.street = street
        self.build = build
        self.apart = apart

    def __str__(self):
        return f"<{self.index}>, <{self.city}>, <{self.street}>, <{self.build}> - <{self.apart}>"