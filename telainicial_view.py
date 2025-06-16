import sys
import tkinter as ttk

class telainicial_view():
    def Tela_inicial(self):
        self.root = ttk.Tk()
        self.root.geometry("1400x1400")

        self.tela_inicial()

        self.root.mainloop()

    def tela_inicial(self): 
        container =  ttk.Frame(relief=ttk.RAISED, borderwidth=1, bg="light grey")
        container.pack(fill=ttk.BOTH, expand=True)

        labelTitulo = ttk.Label(container, width=15, text="Diário Astronômico", bg="light grey", font=("Inter", 25))
        labelTitulo.grid(column=0, row=0, padx=30, pady=0)

        buttonRegistro = ttk.Button(container, text="Fazer registro", bg="Black", fg="white")
        buttonRegistro.grid(column=0, row=1, padx=50, pady=20)
        
        buttonAnalise = ttk.Button(container, text="Ver análise", bg="Black", fg="white")
        buttonAnalise.grid(column=1, row=1, padx=50, pady=20)

        labelLinhaHori = ttk.Label(container, width=100, bg="black")
        labelLinhaHori.grid(column=0, row=2, columnspan=3)

