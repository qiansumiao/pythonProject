car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.get("price", 15000)

print(x)

y = car.get("brand", 1000)
print(y)
