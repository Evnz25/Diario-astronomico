import pymongo

class Model():
    def __init__(self):

        self.meucliente = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.meucliente["DiaAstro"]
        self.registros = self.db["registros"]
    
    def qtd_registros(self):
        qtd_total = self.registros.count_documents({})
        return(qtd_total)
