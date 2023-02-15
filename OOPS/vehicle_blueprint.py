class vehicle():
    def __init__(self, brand, owner, price, colour):
        self.brand = brand
        self.owner = owner
        self.price = price
        self.colour = colour

vehicle_owner_one = vehicle("Land Rover", "Nathnael", "6.5M", "White")
print(vehicle_owner_one.brand)
print(vehicle_owner_one.owner)
print(vehicle_owner_one.price)
print(vehicle_owner_one.colour)

print("----------End of owner 1-----------")

vehicle_owner_two = vehicle("Avensis", "Geofrey", "2.5M", "silver")
print(vehicle_owner_two.brand)
print(vehicle_owner_two.owner)
print(vehicle_owner_two.price)
print(vehicle_owner_two.colour)

print("-----------End of owner 2---------")

vehicle_owner_three = vehicle("Audi", "Rainer", "4.5M", "Black")
print(vehicle_owner_three.brand)
print(vehicle_owner_three.owner)
print(vehicle_owner_three.price)
print(vehicle_owner_three.colour)