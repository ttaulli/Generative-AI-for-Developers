import requests
url = "https://api.chucknorris.io/jokes/random"
params = {"limitTo": "nerdy"}
response = requests.get(url, params)
joke = response.json()["value"]
print(joke)