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
    
    def media_visibilidade(self):
        pipeline = [
            {
                "$group": {
                    "_id": None,
                    "mediaVis": {
                        "$avg": "$Visibilidade"
                    }
                }
            }
        ]

        resultado = list(self.registros.aggregate(pipeline))
        media = resultado[0]["mediaVis"]
        return media

    def salvar_registro(self):
        mydict = {"Astro": self.entryAstro.get(), 
          "Nome": self.entryNome.get(),
          "Data": self.entryData.get(),
          "Horário": self.entryHorario.get(),
          "CoordenadasX": self.Coordenadas.get(),
          "Equipamento": self.entryEquipamento.get(),
          "Visibilidade": self.entryVisibiidade.get(),
          "EscalaBortle": self.entryBortle.get(),
          "Descricao": self.entryDescricao.get()}
        
        x = registros.insert_one(mydict)
