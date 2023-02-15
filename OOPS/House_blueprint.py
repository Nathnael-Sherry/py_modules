class house():
    def __init__(self, location, owner, price, roof):
        self.location = location
        self.owner = owner
        self.price = price
        self.roof = roof

house_owner_one = house("Westlands", "Precious", "6.5M", "98 Pieces")
print(house_owner_one.location)
print(house_owner_one.owner)
print(house_owner_one.price)
print(house_owner_one.roof)

print("----------End of owner 1-----------")
house_owner_two = house("Westlands", "Precious", "6.5M", "98 Pieces")
print(house_owner_two.location)
print(house_owner_two.owner)
print(house_owner_two.price)
print(house_owner_two.roof)