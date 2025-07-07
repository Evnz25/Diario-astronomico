import pymongo
from datetime import datetime

meucliente = pymongo.MongoClient("mongodb://localhost:27017/")

db = meucliente["DiaAstro"]

registros = db["registros"]

salvar_data = "25/06/2025"
salvar_horario = "21:30"

salvar_dia, salvar_mes, salvar_ano = salvar_data.split("/")
hora, minuto = salvar_horario.split(":")
data_obj = datetime(int(salvar_ano), int(salvar_mes), int(salvar_dia), int(hora), int(minuto))

insercao = {
    "Astro": "Planeta", 
    "Nome": "Júpiter",
    "Data": data_obj,
    "Cidade": "Cambé",
    "CoordenadasX": "-22.424319",
    "CoordenadasY": "-45.453345",
    "Equipamento": "Telescópio refletor 130mm",
    "Visibilidade": 4,
    "EscalaBortle": 4,
    "Descricao": "Observação clara de Júpiter.",
    "Caminho_img": r"C:/Users/Alunos/Desktop/Nova pasta/Diario-astronomico/Imagens/Jupiter.jpg"}

x = registros.insert_one(insercao)

insercao = {
    "Astro": "Planeta", 
    "Nome": "Vênus",
    "Data": data_obj,
    "Cidade": "Cambé",
    "CoordenadasX": "-22.687640",
    "CoordenadasY": "-45.733570",
    "Equipamento": "Binóculo 10x50",
    "Visibilidade": 4,
    "EscalaBortle": 3,
    "Descricao": "",
    "Caminho_img": r"C:/Users/Alunos/Desktop/Nova pasta/Diario-astronomico/Imagens/Venus.png"}

x = registros.insert_one(insercao)
