from smartphone import Smartphone

catalog = []

smartphone1 = Smartphone("Samsung", "A100", "+7910")
smartphone2 = Smartphone("Apple", "14 ProMax", "+7920")
smartphone3 = Smartphone("Nokia", "8800", "+7930")
smartphone4 = Smartphone("Apple", "8 Plus", "+7940")
smartphone5 = Smartphone("Honor", "90", "+7950")

catalog.append(smartphone1)
catalog.append(smartphone2)
catalog.append(smartphone3)
catalog.append(smartphone4)
catalog.append(smartphone5)

for smartphone in catalog:
    smartphone.show_all()
