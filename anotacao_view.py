import sys
import tkinter as ttk

class Anotacao_view():
    def __init__(self):
        self.root = ttk.Tk()
        self.root.geometry("700x500")

        self.anotacao_dadosbasico()

        self.anotacao_descricao()

        self.root.mainloop()

    def anotacao_dadosbasico(self):
        container = ttk.Frame(relief=ttk.RAISED, borderwidth=1, bg="light grey")
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


    def anotacao_descricao(self):
        container = ttk.Frame(relief=ttk.RAISED, borderwidth=1, bg="light grey")
        container.pack(fill=ttk.BOTH, expand=True)

        labelDescricao = ttk.Label(container, width=15, text="Descrição: ", bg="light grey")
        labelDescricao.grid(column=0, row=0, padx=5, pady=0)

        self.entryDescricao = ttk.Text(container, width=60, height=10)
        self.entryDescricao.grid(column=1, row=1, padx=5, pady=0)


if __name__ == "__main__":
    Anotacao_view()