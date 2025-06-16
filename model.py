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

    def salvar_registro(self, salvar_astro, salvar_nomeregistro, salvar_data, salvar_horario, salvar_coordenadas, salvar_equipamento, salvar_visibilidade, salvar_escalabortle, salvar_descricao):
        mydict = {"Astro": salvar_astro, 
          "Nome": salvar_nomeregistro,
          "Data": salvar_data,
          "Horário": salvar_horario,
          "CoordenadasX": salvar_coordenadas,
          "Equipamento": salvar_equipamento,
          "Visibilidade": salvar_visibilidade,
          "EscalaBortle": salvar_escalabortle,
          "Descricao": salvar_descricao}
        
        x = self.registros.insert_one(mydict)


