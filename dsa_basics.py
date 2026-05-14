cities = ["Berlin", "Vienna", "Graz", "Zagreb", "Sarajevo"]
cities.append("Ljubljana")
cities.pop(0)
print(cities)

personal_info = {"name": "Filip", "age": 32, "city": "Graz"}
personal_info["is_student"] = True
print(personal_info["city"])
print(personal_info.keys())
print(personal_info.values())

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a.intersection(b))
print(a.union(b))
print(a.difference(b))