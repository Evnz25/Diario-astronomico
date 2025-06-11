import pymongo

meucliente = pymongo.MongoClient("mongodb://localhost:27017/")

db = meucliente["DiaAstro"]

registros = db["registros"]

mydict = {"Astro": "Costelação", 
          "Nome": "Costelação de Órion",
          "Data": "25/04/2025",
          "Horário": "20:00",
          "CoordenadasX": "-23.169614",
          "CoordenadasY": "-50.636040",
          "Equipamento": "Binóculo",
          "Visibilidade": 5,
          "EscalaBortle": 1,
          "Descricao": "Registro da constelação de Órion de ponta cabeça"}

x = registros.insert_one(mydict)

mydict = {"Astro": "Costelação", 
          "Nome": "Costelação de Órion",
          "$Data": "2025-04-25",
          "Horário": "20:00",
          "CoordenadasX": "-23.169614",
          "CoordenadasY": "-50.636040",
          "Equipamento": "Binóculo",
          "Visibilidade": 2,
          "EscalaBortle": 1,
          "Descricao": "Registro da constelação de Órion de ponta cabeça"}


x = registros.insert_one(mydict)

print(db.list_collection_names())

print(meucliente.list_database_names()) 

quantidade_total = registros.count_documents({})
print(f"A quantidade total de registros é: {quantidade_total}")
