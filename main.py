import requests, json
from clothing import Clothing
from fit import fit

# Get the weather data
if False:
    api_key = "b26a73f4c36c4a00a17193053240711"
    base_url = "http://api.weatherapi.com/v1/current.json"

    city_name = input("Enter city name : ")
    
    complete_url = base_url + "?key=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)

    x = response.json()
    print(x)


# Load all the clothings into the program
allclothing = {}

for part in ["tops", "bottoms", "accessories"]:
    allclothing[part] = []
    w = open(f"weights/{part}", "r")
    filelines = w.readlines()

    for line in filelines:
        allclothing[part].append(Clothing(line.split(" ")[0], float(line.split(" ")[1]), part))

#print(allclothing)

combos = fit(allclothing["tops"], allclothing["bottoms"], allclothing["accessories"], 15)


for i in combos:
    total = ""
    for x in i:
        total += str(x) + " -> "
    print(total)