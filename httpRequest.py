import requests
response = requests.get('http://api.open-notify.org/astros.json')
resp = response.json()
people = resp["people"]
print("People in space are:\n")
for person in (people):
    print(person["name"])
    #print(person)