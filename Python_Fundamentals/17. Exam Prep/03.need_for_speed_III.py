n = int(input())
collection = {}

for cars in range(n):
    car, mileage, fuel = input().split("|")
    collection[car] = {"mileage": int(mileage), "fuel": int(fuel)}

command = input()
while command != "Stop":
    operation = command.split(" : ")
    if operation[0] == "Drive":
        car = operation[1]
        distance = int(operation[2])
        fuel = int(operation[3])
        if collection[car]["fuel"] < fuel:
            print(f"Not enough fuel to make that ride")
        else:
            collection[car]["fuel"] -= fuel
            collection[car]["mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if collection[car]["mileage"] >= 100000:
            print(f"Time to sell the {car}!")
            del collection[car]

    elif operation[0] == "Refuel":
        car = operation[1]
        fuel = int(operation[2])
        added = min(fuel, 75 - collection[car]["fuel"])
        collection[car]["fuel"] += added
        print(f"{car} refueled with {added} liters")


    elif operation[0] == "Revert":
        car = operation[1]
        kilometers = int(operation[2])
        collection[car]["mileage"] -= kilometers
        if collection[car]["mileage"] < 10000:
            collection[car]["mileage"] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

for car, car_data in collection.items():
    mileage = car_data["mileage"]
    fuel = car_data["fuel"]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")