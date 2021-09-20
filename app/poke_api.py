
import requests

class Pokemon:

    def all_pokemon(self):
        url = "https://pokeapi.co/api/v2/pokemon?limit=151"
        response = requests.get(url)
        return response.json()

    def get_pokemon(self, pokemon):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
        response = requests.get(url)
        if ("Not Found" in response.text):
            return f"Pokémon {pokemon} not found."
        return response.json()


poke = Pokemon()
# print(poke.all_pokemon())
print(poke.get_pokemon("charmandeR"))
# print(poke.get_pokemon("charmander"))
