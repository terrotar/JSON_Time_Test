
import requests


class Pokemon:

    def all(self):
        url = "https://pokeapi.co/api/v2/pokemon?limit=151"
        response = requests.get(url)
        return response.json()


poke = Pokemon()
print(poke.all())
