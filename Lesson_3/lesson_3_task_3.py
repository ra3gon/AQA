from address import Address
from mailing import Mailing

to_address = Address ("150000", "Yaroslavl", "Lenina", "1", "2")
from_address = Address ("100777", "Moscow", "Maroseyka", "12", "77")

mail = Mailing(from_address = from_address, to_address = to_address, cost=1000, track="ABC019283")

print (mail)


