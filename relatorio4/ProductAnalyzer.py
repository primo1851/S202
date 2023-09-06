from bson import SON
from database import Database
from writeAJson import writeAJson

db = Database(database="mercado", collection="compras")
db.resetDatabaseAndPopulate()


class ProductAnalyzer:
    def totalSales(self):
        pipeline = [
            {
                "$group": {
                    "_id": {"data": "$data_compra"},
                    "total_vendas": {"$sum": 1},
                },
            },
        ]
        result = list(db.collection.aggregate(pipeline))
        writeAJson(result, "Vendas totais")

    def bestSeller(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {
                "$group": {
                    "_id": "$produtos.descricao",
                    "total_vendido": {"$sum": "$produtos.quantidade"},
                },
            },
            {"$sort": {"total_vendido": -1}},
            {"$limit": 1},
        ]
        result = db.collection.aggregate(pipeline)
        if result:
            writeAJson(result, "Melhor em vendas")
        else:
            writeAJson(None, "Melhor em vendas")

    def bestConsumer(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {
                "$group": {
                    "_id": {"cliente": "$cliente_id", "data": "$data_compra"},
                    "total": {
                        "$sum": {
                            "$multiply": ["$produtos.quantidade", "$produtos.preco"]
                        }
                    },
                }
            },
            {"$sort": {"_id.data": 1, "total": -1}},
            {
                "$group": {
                    "_id": "$_id.data",
                    "cliente": {"$first": "$_id.cliente"},
                    "total": {"$first": "$total"},
                }
            },
        ]
        result = db.collection.aggregate(pipeline)
        if result:
            writeAJson(result, "Melhor consumidor")  # type: ignore
        else:
            writeAJson(None, "Melhor consumidor")

    def inStock(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {
                "$group": {
                    "_id": "$produtos.descricao",
                    "total_quantidade_vendida": {"$sum": "$produtos.quantidade"},
                },
            },
            {"$match": {"total_quantidade_vendida": {"$gt": 1}}},
        ]
        result = db.collection.aggregate(pipeline)
        writeAJson(result, "Em estoque")
