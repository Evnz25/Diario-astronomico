import pymongo

meucliente = pymongo.MongoClient("mongodb://localhost:27017/")

db = meucliente["DiaAstro"]

registros = db["registros"]

insercao = {"Astro": "Costelação", 
          "Nome": "Costelação de Órion",
          "Data": "25/06/2025 21:30",
          "Cidade": "Londrina",
          "CoordenadasX": "-23.169614",
          "CoordenadasY": "-50.636040",
          "Equipamento": "Binóculo",
          "Visibilidade": 5,
          "EscalaBortle": 1,
          "Descricao": "Registro da constelação de Órion de ponta cabeça",
          "Caminho_img": r"C:\Users\Usuario\Desktop\Backup area de trabalho\Tads\Diário Astronômico\Astronomical-Diary\Imagens\Costelacao.png"}

x = registros.insert_one(insercao)

insercao = {
    "Astro": "Planeta", 
    "Nome": "Júpiter e suas Luas Galileanas",
    "Data": "15/06/2025 21:30",
    "Cidade": "Cambé",
    "CoordenadasX": "-22.424319",
    "CoordenadasY": "-45.453345",
    "Equipamento": "Telescópio refletor 130mm",
    "Visibilidade": 4,
    "EscalaBortle": 4,
    "Descricao": "Observação clara de Júpiter.",
    "Caminho_img": r"C:\Users\Usuario\Desktop\Backup area de trabalho\Tads\Diário Astronômico\Astronomical-Diary\Imagens\Jupiter.jpg"}

x = registros.insert_one(insercao)

insercao = {
    "Astro": "Planeta", 
    "Nome": "Marte",
    "Data": "28/06/2025",
    "Horário": "20:45",
    "Cidade": "Cambé",
    "CoordenadasX": "-22.687640",
    "CoordenadasY": "-45.733570",
    "Equipamento": "Binóculo 10x50",
    "Visibilidade": 4,
    "EscalaBortle": 3,
    "Descricao": ""}