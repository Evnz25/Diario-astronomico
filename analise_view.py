import sys
import tkinter as ttk

from controller import Controller

class analise_view():
    def __init__(self):
        self.root = ttk.Tk()
        self.root.geometry("700x500")
        
        self.controller = Controller(self)
        
        self.dados_gerais()
        
        self.root.mainloop()
        
    def dados_gerais(self):
        container = ttk.Frame(relief=ttk.RAISED, borderwidth=1, bg="light grey")
        container.pack(fill=ttk.BOTH, expand=True)
        
        self.labelQtd = ttk.Label(container, width=10, text="Número de registros: {Qtd}", bg="light grey")
        self.labelQtd.grid(column=0, row=0, padx=5, pady=5)
        
        Qtd = self.controller.astro_mais_observado_controller()
        
    def update_viewx(self, text):
        self.labelQtd['text'] = text

if __name__ == "__main__":
    analise_view()
        