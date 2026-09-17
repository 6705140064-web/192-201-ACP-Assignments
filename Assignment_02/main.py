from rental import Vehicle, Renter, ElectricCar, Motorbike


# Create vehicles
car = Vehicle("Toyota", "Yaris", "1AB234")
electric = ElectricCar("Tesla", "Model 3", "EV1234", 75)
motorbike = Motorbike("Honda", "CBR500R", "MB5678", 500)


# Create a renter
renter = Renter("John", 12345)

print("Renter:", renter.name)
print("License:", renter.license_no)
print("Rented list:", renter.rented)

print("\nVehicle before renting:")
print(car)

# Rent and return a vehicle
car.rent()
renter.rented.append(car)

print("\nVehicle after renting:")
print(car)

car.return_vehicle()
renter.rented.remove(car)

print("\nVehicle after returning:")
print(car)


# Test invalid renter name
print("\nTesting invalid name:")
try:
    bad_renter = Renter("", 12345)
except ValueError as e:
    print("ValueError:", e)


# Test invalid license
print("\nTesting invalid license:")
try:
    bad_renter = Renter("Alice", 0)
except ValueError as e:
    print("ValueError:", e)


# Test changing license later
print("\nTesting license change:")
try:
    renter.license_no = -10
except ValueError as e:
    print("ValueError:", e)


# Inheritance
print("\nInheritance:")
print("ElectricCar is Vehicle:", isinstance(electric, Vehicle))
print("Motorbike is Vehicle:", isinstance(motorbike, Vehicle))


# Polymorphism
print("\nPolymorphism:")
vehicles = [car, electric, motorbike]

for vehicle in vehicles:
    print(vehicle)

    