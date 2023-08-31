from pokedex import Pokedex
from writeAJson import writeAJson

writeAJson(Pokedex().getPokemonsByType("Fire"), "Types")
writeAJson(Pokedex().getPokemonsBetweenId("19", "51"), "IDs")
writeAJson(Pokedex().getPokemonsByEggDistance("2 km"), "Eggs")
writeAJson(Pokedex().getPokemonsByHeight("1.80 m"), "Height")
writeAJson(
    Pokedex().getPokemonsByPreviousEvolution("004", "Charmander"),
    "PreviousEvolution",
)
