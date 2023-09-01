from database import Database

db = Database(database="pokedex", collection="pokemons")


class Pokedex:
    def getPokemonsByType(self, firstTypeParams):
        return db.collection.find({"type": firstTypeParams})

    def getPokemonsBetweenId(self, lowestNumIDParams, highestNumIDParams):
        return db.collection.find(
            {
                "id": {
                    "$gt": lowestNumIDParams,
                    "$lt": highestNumIDParams,
                }
            }
        )

    def getPokemonsByEggDistance(self, eggParams):
        return db.collection.find({"egg": eggParams})

    def getPokemonsByHeight(self, heightParams):
        return db.collection.find({"height": heightParams})

    def getPokemonsByPreviousEvolution(self, nameParams):
        return db.collection.find(
            {"name": nameParams, "prev_evolution": {"$exists": True}}
        )
