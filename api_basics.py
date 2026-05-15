import requests

respond = requests.get("https://jsonplaceholder.typicode.com/users")
print(respond.status_code)

for user in respond.json():
    print(f"{user["name"]} - {user["email"]}")