import pymongo
from datetime import datetime
from bson.objectid import ObjectId

Meses = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho",
    7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}

class Model():
    def __init__(self):
        self.meucliente = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.meucliente["DiaAstro"]
        self.registros = self.db["registros"]

    def pegar_registro_por_id(self, registro_id):
        try:
            obj_id = ObjectId(registro_id)
            registro = self.registros.find_one({"_id": obj_id})
            return registro
        except Exception as e:
            print(f"Erro ao buscar registro por ID: {e}")
            return None
    
    def pegar_registros(self):
        return list(self.registros.find().sort("Data", -1))

    def qtd_registros(self):
        qtd_total = self.registros.count_documents({})
        return qtd_total

    def astro_mais_observado(self):
        pipeline = [
            {"$group": {"_id": "$Astro", "quantidade": {"$sum": 1}}},
            {"$sort": {"quantidade": -1}},
            {"$limit": 1}
        ]
        resultado = list(self.registros.aggregate(pipeline))
        if not resultado: return "N/D"
        return resultado[0]['_id']
    
    def media_visibilidade(self):
        pipeline = [
            {"$group": {"_id": None, "mediaVis": {"$avg": "$Visibilidade"}}}
        ]
        resultado = list(self.registros.aggregate(pipeline))
        if not resultado: return 0
        return round(resultado[0]["mediaVis"], 2)
    
    def mes_de_mais_observacao(self):
        if self.registros.count_documents({}) == 0: return "N/D"
        pipeline = [
            {"$project": {"mes": {"$month": "$Data"}}},
            {"$group": {"_id": "$mes", "contagem": {"$sum": 1}}},
            {"$sort": {"contagem": -1}},
            {"$limit": 1}
        ]
        resultado = list(self.registros.aggregate(pipeline))
        if not resultado: return "N/D"
        return Meses.get(resultado[0]['_id'], "N/D")
    
    def mes_de_melhor_visibilidade(self):
        if self.registros.count_documents({}) == 0: return "N/D"
        pipeline = [
            {"$group": {"_id": {"$month": "$Data"}, "media_visibilidade": {"$avg": "$Visibilidade"}}},
            {"$sort": {"media_visibilidade": -1}},
            {"$limit": 1}
        ]
        resultado = list(self.registros.aggregate(pipeline))
        if not resultado: return "N/D"
        return Meses.get(resultado[0]['_id'], "N/D")
    
    def anotacao_melhor_visibilidade(self):
        if self.registros.count_documents({}) == 0: return None
        melhor_registro = self.registros.find_one(sort=[("Visibilidade", -1)])
        return melhor_registro

    def salvar_registro(self, salvar_astro, salvar_nomeregistro, salvar_data, salvar_horario, salvar_cidade, salvar_coordenadasX, salvar_coordenadasY, salvar_equipamento, salvar_visibilidade, salvar_escalabortle, salvar_descricao, salvar_caminho_img):
        try:
            salvar_dia, salvar_mes, salvar_ano = salvar_data.split("/")
            hora, minuto = salvar_horario.split(":")
            data_obj = datetime(int(salvar_ano), int(salvar_mes), int(salvar_dia), int(hora), int(minuto))

            mydict = {
                "Astro": salvar_astro, 
                "Nome": salvar_nomeregistro,
                "Data": data_obj,
                "Cidade": salvar_cidade,
                "CoordenadasX": salvar_coordenadasX,
                "CoordenadasY": salvar_coordenadasY,
                "Equipamento": salvar_equipamento,
                "Visibilidade": int(salvar_visibilidade),
                "EscalaBortle": int(salvar_escalabortle),
                "Descricao": salvar_descricao,
                "Caminho_img": salvar_caminho_img
            }
            
            self.registros.insert_one(mydict)
            return True

        except (ValueError, TypeError) as e:
            print(f"Erro ao criar data ou converter valores: {e}")
            return False
        
    def deletar_registro(self, registro_id):
        """Deleta um documento da coleção pelo seu _id."""
        try:
            obj_id = ObjectId(registro_id)
            resultado = self.registros.delete_one({"_id": obj_id})
            
            if resultado.deleted_count == 1:
                return True 
            else:
                return False 
        except Exception as e:
            print(f"Erro ao deletar registro: {e}")
            return False
        
    def pegar_cidades_por_bortle(self, bortle_valor):
        try:
            valor_float = float(bortle_valor)
            
            query = {"EscalaBortle": valor_float}
            
            cidades_encontradas = self.registros.distinct("Cidade", query)
            
            return cidades_encontradas
        except (ValueError, TypeError) as e:
            print(f"Erro ao converter valor Bortle ou ao buscar cidades: {e}")
            return [] 