import pymongo

class Model():
    def __init__(self):

        self.meucliente = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.meucliente["DiaAstro"]
        self.registros = self.db["registros"]
    
    def qtd_registros(self):
        qtd_total = self.registros.count_documents({})
        return qtd_total

    def astro_mais_observado(self):
        pipeline = [
            {
                "$group": {
                    "_id": "$Astro",
                    "quantidade": {"$sum": 1}
                }
            },
            {
                "$sort":{
                    "quantidade": -1
                }
            },
            {
                "$limit": 1
            }
        ]

        resultado = list(self.registros.aggregate(pipeline))
        astro_comum = resultado[0]
        astro_comum_nome = astro_comum['_id']
        return astro_comum_nome
    
    
