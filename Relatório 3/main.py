from pokedex import Pokedex
from writeAJson import writeAJson

writeAJson(Pokedex().getPokemonsByType("Fire"), "Types")
writeAJson(Pokedex().getPokemonsBetweenId(121, 151), "IDs")
writeAJson(Pokedex().getPokemonsByEggDistance("2 km"), "Eggs")
writeAJson(Pokedex().getPokemonsByHeight("0.61 m"), "Height")
writeAJson(
    Pokedex().getPokemonsByPreviousEvolution("Kakuna"),
    "PreviousEvolution",
)
