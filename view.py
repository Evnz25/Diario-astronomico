import sys
import tkinter as ttk
from controller import Controller

class View():
    def __init__(self):
        self.root = ttk.Tk()
        self.root.geometry("1400x1400")

        self.controller = Controller(self)

        self.container =  ttk.Frame(self.root)
        self.container.pack()

        self.criar_tela_inicial()
        self.criar_tela_analise()
        self.criar_tela_anotacao()

        self.tela_inicial.grid(row=0, column=0, sticky='nsew')
        self.tela_analise.grid(row=0, column=0, sticky='nsew')
        self.tela_anotacao.grid(row=0, column=0, sticky='nsew')

        self.mostrar_tela_inicial()

        self.root.bind('<Escape>', self.fechar)

        self.root.mainloop()

    def fechar(self):
        sys.exit()

    def mostrar_tela_inicial(self):
        self.tela_inicial.tkraise()
    
    def mostrar_tela_analise(self):
        self.tela_analise.tkraise()

    def mostrar_tela_anotacao(self):
        self.tela_anotacao.tkraise()

    def criar_tela_inicial(self): 
        container =  ttk.Frame(self.container,relief=ttk.RAISED, borderwidth=1, bg="light grey")
        container.pack(fill=ttk.BOTH, expand=True)

        labelTitulo = ttk.Label(container, width=15, text="Diário Astronômico", bg="light grey", font=("Inter", 25))
        labelTitulo.grid(column=0, row=0, padx=30, pady=0)

        buttonRegistro = ttk.Button(container, text="Fazer registro", bg="Black", fg="white")
        buttonRegistro.grid(column=0, row=1, padx=50, pady=20)
        
        buttonAnalise = ttk.Button(container, text="Ver análise", bg="Black", fg="white")
        buttonAnalise.grid(column=1, row=1, padx=50, pady=20)

        labelLinhaHori = ttk.Label(container, width=100, bg="black")
        labelLinhaHori.grid(column=0, row=2, columnspan=3)

    def criar_tela_analise(self):
        container =  ttk.Frame(self.container, relief=ttk.RAISED, borderwidth=1, bg="light grey")
        container.pack(fill=ttk.BOTH, expand=True)
            
        self.labelQtd = ttk.Label(container, width=10, text="Número de registros: {Qtd}", bg="light grey")
        self.labelQtd.grid(column=0, row=0, padx=5, pady=5)
            
        #Qtd = self.controller.media_visibilidade_controller()
    
    def criar_tela_anotacao(self):
        container =  ttk.Frame(self.container, relief=ttk.RAISED, borderwidth=1, bg="light grey")
        container.pack(fill=ttk.BOTH, expand=True)

        labelAstro = ttk.Label(container, width=10, text="Astros: ", bg="light grey")
        labelAstro.grid(column=0, row=0, padx=5, pady=5)

        self.entryAstro = ttk.Entry(container, width=20)
        self.entryAstro.grid(column=1, row=0, padx=0, pady=5)

        labelNomeRegistro = ttk.Label(container, width=15, text="Nome do registro: ", bg="light grey")
        labelNomeRegistro.grid(column=0, row=1, padx=5, pady=5)

        self.entryNomeRegistro = ttk.Entry(container, width=20)
        self.entryNomeRegistro.grid(column=1, row=1, padx=0, pady=5)

        labelData = ttk.Label(container, width=15, text="Data: ", bg="light grey")
        labelData.grid(column=0, row=2, padx=5, pady=5)

        self.entryData = ttk.Entry(container, width=20)
        self.entryData.grid(column=1, row=2, padx=0, pady=5)

        labelHorario = ttk.Label(container, width=15, text="Horario: ", bg="light grey")
        labelHorario.grid(column=0, row=3, padx=5, pady=5)

        self.entryHorario = ttk.Entry(container, width=20)
        self.entryHorario.grid(column=1, row=3, padx=0, pady=5)

        labelCoordenadas = ttk.Label(container, width=15, text="Coordenas: ", bg="light grey")
        labelCoordenadas.grid(column=0, row=4, padx=5, pady=5)

        self.entryCoordenadas = ttk.Entry(container, width=20)
        self.entryCoordenadas.grid(column=1, row=4, padx=0, pady=5)

        labelEquipamento = ttk.Label(container, width=15, text="Equipamento: ", bg="light grey")
        labelEquipamento.grid(column=0, row=5, padx=5, pady=5)

        self.entryEquipamento = ttk.Entry(container, width=20)
        self.entryEquipamento.grid(column=1, row=5, padx=0, pady=5)

        labelVisibilidade = ttk.Label(container, width=15, text="Visibilidade: ", bg="light grey")
        labelVisibilidade.grid(column=0, row=6, padx=5, pady=5)

        self.visibilidade = ttk.DoubleVar()

        escalaVisibilidade = ttk.Scale(container, from_=1, to=5, width=12, length=160, variable=self.visibilidade,
                                       orient=ttk.HORIZONTAL, bg="light grey")
        escalaVisibilidade.grid(column=1, row=6, padx=0, pady=5)

        labelBortle = ttk.Label(container, width=15, text="Escala Bortle: ", bg="light grey")
        labelBortle.grid(column=0, row=7, padx=5, pady=5)

        self.bortle = ttk.DoubleVar()

        escalaBortle = ttk.Scale(container, from_=1, to=8, width=12, length=200, variable=self.bortle,
                                       orient=ttk.HORIZONTAL, bg="light grey")
        escalaBortle.grid(column=1, row=7, padx=0, pady=5)

        labelDescricao = ttk.Label(container, width=15, text="Descrição: ", bg="light grey")
        labelDescricao.grid(column=0, row=0, padx=5, pady=0)

        self.entryDescricao = ttk.Text(container, width=60, height=10)
        self.entryDescricao.grid(column=1, row=1, padx=5, pady=0)

        buttonSalvar = ttk.Button(
            container,
            text="Salvar",
            bg="Black",
            fg="white",
            command=self.salvar_registros)
        buttonSalvar.grid(column=4, row=2, padx=50, pady=20, ipadx=7, ipady=3) 

    def salvar_registros(self):
        salvar_astro = self.entryAstro.get()
        salvar_nomeregistro = self.entryNomeRegistro.get()
        salvar_data = self.entryData.get()
        salvar_horario = self.entryHorario.get()
        salvar_coordenadas = self.entryCoordenadas.get()
        salvar_equipamento = self.entryEquipamento.get()
        salvar_visibilidade = self.visibilidade.get()
        salvar_escalabortle = self.bortle.get()
        salvar_descricao = self.entryDescricao.get("1.0", "end")
        self.controller.salvar_registro_controller(salvar_astro, salvar_nomeregistro, salvar_data, salvar_horario, salvar_coordenadas, salvar_equipamento, salvar_visibilidade, salvar_escalabortle, salvar_descricao)


if __name__ == "__main__":
    View()