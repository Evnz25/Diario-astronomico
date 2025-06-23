import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from controller import Controller
from PIL import Image, ImageTk

class View():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Diário Astronômico (Versão Original Corrigida)")
        self.root.geometry("800x600")

        self.controller = Controller(self)

        # 1. Container principal que vai segurar as telas empilhadas
        # Usamos 'grid' aqui para permitir que as telas sobrepostas preencham o espaço.
        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # 2. Chamar a criação de cada tela, uma por uma
        self.criar_tela_inicial()
        self.criar_tela_analise()
        self.criar_tela_anotacao()
        
        # 3. Mostrar a tela inicial primeiro
        self.mostrar_tela_inicial()

        self.root.bind('<Escape>', self.fechar)
        self.root.mainloop()

    def fechar(self, event=None):
        sys.exit()

    # --- Funções para trocar de tela ---
    def mostrar_tela_inicial(self):
        self.tela_inicial.tkraise()
    
    def mostrar_tela_analise(self):
        # Aqui você pode adicionar lógica para atualizar os dados antes de mostrar
        print("Mostrando tela de análise...")
        self.tela_analise_container.tkraise()

    def mostrar_tela_anotacao(self):
        self.tela_anotacao.tkraise()

    # --- Métodos para criar cada tela ---
    def criar_tela_inicial(self):
            # --- Configuração do Frame principal da tela ---
        self.tela_inicial = tk.Frame(self.container, bg="#F0F0F0")
        self.tela_inicial.grid(row=0, column=0, sticky='nsew')

        # --- 1. Seção do Cabeçalho ---
        header_frame = tk.Frame(self.tela_inicial, bg="#F0F0F0")
        header_frame.pack(pady=20, padx=40, fill='x')

        label_titulo = ttk.Label(header_frame, text="Diário Astronômico", 
                                font=("Inter", 28, "bold"), background="#F0F0F0")
        label_titulo.pack(anchor='w')
        
        botoes_frame = tk.Frame(header_frame, bg="#F0F0F0")
        botoes_frame.pack(anchor='w', pady=15)

        # --- CORREÇÃO NO ESTILO DOS BOTÕES ---
        style = ttk.Style()
        # Força o uso do tema 'clam', que é mais customizável em todos os sistemas
        try:
            style.theme_use('clam')
        except tk.TclError:
            # Se 'clam' não estiver disponível, usa o padrão
            pass

        style.configure("Dark.TButton",
                        background="#333333",
                        foreground="white",
                        font=("Inter", 10, "bold"),
                        padding=(15, 8),
                        bordercolor="#333333") # Garante que a borda tenha a mesma cor
        style.map("Dark.TButton",
                background=[('active', '#555555')],
                bordercolor=[('active', '#555555')])

        btn_registro = ttk.Button(botoes_frame, text="Fazer registro", style="Dark.TButton",
                                command=self.mostrar_tela_anotacao)
        btn_registro.pack(side="left")

        btn_analise = ttk.Button(botoes_frame, text="Ver análise", style="Dark.TButton",
                                command=self.mostrar_tela_analise)
        btn_analise.pack(side="left", padx=10)

        # --- 2. Linha Separadora ---
        separator = tk.Frame(self.tela_inicial, height=20, bg="black")
        separator.pack(fill='x')


    def criar_tela_analise(self):
        # --- Configuração do Frame principal da tela ---
        # Usamos um Frame com padding para criar a borda azul ao redor
        self.tela_analise_container = tk.Frame(self.container, bg="#0078D7", bd=2)
        self.tela_analise_container.grid(row=0, column=0, sticky='nsew')
        
        self.tela_analise = tk.Frame(self.tela_analise_container, bg="#F0F0F0")
        self.tela_analise.pack(fill="both", expand=True, padx=1, pady=1)

        # --- Container principal para o conteúdo, com rolagem ---
        # Isso garante que se o conteúdo for muito grande, o usuário pode rolar
        canvas = tk.Canvas(self.tela_analise, bg="#F0F0F0", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.tela_analise, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#F0F0F0")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # --- 1. Cartão de Dados Gerais ---
        card_dados_gerais = tk.Frame(scrollable_frame, bg="white", relief="solid", bd=1, highlightbackground="#D0D0D0", highlightthickness=1)
        card_dados_gerais.pack(pady=(20, 10), padx=40, fill='x')
        
        content_gerais = tk.Frame(card_dados_gerais, bg="white")
        content_gerais.pack(padx=20, pady=15, anchor="w")

        ttk.Label(content_gerais, text="Dados gerais", font=("Inter", 14, "bold"), background="white").pack(anchor='w', pady=(0, 10))
        ttk.Label(content_gerais, text="Número de registros: 2", font=("Inter", 11), background="white").pack(anchor='w')
        ttk.Label(content_gerais, text="Astro mais observado: Constelações", font=("Inter", 11), background="white").pack(anchor='w')
        ttk.Label(content_gerais, text="Mês de mais observação: Abril", font=("Inter", 11), background="white").pack(anchor='w')

        # --- 2. Cartão de Visibilidade ---
        card_visibilidade = tk.Frame(scrollable_frame, bg="white", relief="solid", bd=1, highlightbackground="#D0D0D0", highlightthickness=1)
        card_visibilidade.pack(pady=10, padx=40, fill='x')

        content_visibilidade = tk.Frame(card_visibilidade, bg="white")
        content_visibilidade.pack(padx=20, pady=15, anchor="w")

        ttk.Label(content_visibilidade, text="visibilidade", font=("Inter", 14, "bold"), background="white").pack(anchor='w', pady=(0, 10))
        ttk.Label(content_visibilidade, text="visibilidade média: 5", font=("Inter", 11), background="white").pack(anchor='w')
        ttk.Label(content_visibilidade, text="Mês de melhor visibilidade: Abril", font=("Inter", 11), background="white").pack(anchor='w', pady=(0, 5))

        # Frame para a barra de Bortle
        bortle_frame = tk.Frame(content_visibilidade, bg="white")
        bortle_frame.pack(fill="x", pady=5)
        ttk.Label(bortle_frame, text="Localizações pela escala Bortle:", font=("Inter", 11), background="white").pack(side="left", anchor='w')
        
        # Barra de progresso para simular a escala
        style_bortle = ttk.Style()
        style_bortle.configure("Bortle.Horizontal.TProgressbar", troughcolor='#E0E0E0', background='#5DADE2', thickness=20)
        bortle_bar = ttk.Progressbar(bortle_frame, orient="horizontal", length=300, mode='determinate', style="Bortle.Horizontal.TProgressbar")
        bortle_bar['value'] = 40 # Exemplo de valor
        bortle_bar.pack(side="left", padx=10, expand=True, fill="x")
        
        # Exemplo de coordenadas (usando um Text para permitir seleção)
        coord_text = tk.Text(content_visibilidade, height=2, width=60, relief="flat", background="white", font=("Courier", 9))
        coord_text.insert("1.0", "X: -23.169614, Y: -50.636040; X: -24.176355, Y: -53.042433")
        coord_text.configure(state="disabled") # Para não ser editável
        coord_text.pack(anchor="w", pady=5)

        # --- 3. Anotação de melhor visibilidade ---
        melhor_anotacao_frame = tk.Frame(scrollable_frame, bg="#F0F0F0")
        melhor_anotacao_frame.pack(pady=(20, 10), padx=40, fill='x')

    def criar_tela_anotacao(self):
        # Frame principal da tela, com uma cor de fundo cinza clara
        self.tela_anotacao = tk.Frame(self.container, bg="#E0E0E0")
        self.tela_anotacao.grid(row=0, column=0, sticky='nsew')

        # --- Frame para conter o formulário com padding ---
        # Isso ajuda a manter as bordas da janela livres
        form_container = ttk.Frame(self.tela_anotacao, style="TFrame")
        form_container.pack(fill="both", expand=True, padx=20, pady=20)

        # Configurar o grid para que as colunas de entrada de texto se expandam
        form_container.grid_columnconfigure(1, weight=1)
        form_container.grid_columnconfigure(3, weight=1)
        form_container.grid_columnconfigure(4, weight=1)
        form_container.grid_rowconfigure(8, weight=1) # Permite que a descrição se expanda verticalmente

        # --- Linha 1: Astros ---
        ttk.Label(form_container, text="Astros:").grid(row=0, column=0, sticky="w", pady=5)
        self.entryAstro = ttk.Entry(form_container)
        self.entryAstro.grid(row=0, column=1, columnspan=3, sticky="ew", padx=(5, 0))

        # --- Linha 2: Nome do registro ---
        ttk.Label(form_container, text="Nome do registro:").grid(row=1, column=0, sticky="w", pady=5)
        self.entryNomeRegistro = ttk.Entry(form_container)
        self.entryNomeRegistro.grid(row=1, column=1, columnspan=3, sticky="ew", padx=(5, 0))

        # --- Linha 3: Data e Horário ---
        ttk.Label(form_container, text="Data:").grid(row=2, column=0, sticky="w", pady=5)
        self.entryData = ttk.Entry(form_container)
        self.entryData.grid(row=2, column=1, sticky="ew", padx=5)

        ttk.Label(form_container, text="Horário:").grid(row=2, column=2, sticky="w", pady=5)
        self.entryHorario = ttk.Entry(form_container)
        self.entryHorario.grid(row=2, column=3, sticky="ew", padx=5)

        # --- Linha 4: Coordenadas ---
        ttk.Label(form_container, text="Coordenadas").grid(row=3, column=0, sticky="w", pady=5)
        ttk.Label(form_container, text="X:").grid(row=3, column=0, sticky="e", padx=(0,5))
        self.entryCoordenadasX = ttk.Entry(form_container)
        self.entryCoordenadasX.grid(row=3, column=1, sticky="ew", padx=5)

        ttk.Label(form_container, text="Y:").grid(row=3, column=2, sticky="w", pady=5)
        self.entryCoordenadasY = ttk.Entry(form_container)
        self.entryCoordenadasY.grid(row=3, column=3, sticky="ew", padx=5)
        
        # --- Linha 5: Equipamento ---
        ttk.Label(form_container, text="Equipamento:").grid(row=4, column=0, sticky="w", pady=5)
        self.entryEquipamento = ttk.Entry(form_container)
        self.entryEquipamento.grid(row=4, column=1, columnspan=3, sticky="ew", padx=(5, 0))

        # --- Linha 6: Visibilidade ---
        ttk.Label(form_container, text="Visibilidade:").grid(row=5, column=0, sticky="w", pady=5)
        self.visibilidade = tk.DoubleVar()
        self.scale_visibilidade = ttk.Scale(form_container, from_=1, to=5, variable=self.visibilidade)
        self.scale_visibilidade.grid(row=5, column=1, columnspan=2, sticky="ew", padx=5)
        self.spin_visibilidade = ttk.Spinbox(form_container, from_=1, to=5, textvariable=self.visibilidade, width=5)
        self.spin_visibilidade.grid(row=5, column=3, sticky="w")
        
        # --- Linha 7: Escala de Bortle ---
        ttk.Label(form_container, text="Escala de Bortle:").grid(row=6, column=0, sticky="w", pady=5)
        self.bortle = tk.DoubleVar(value=8)
        self.scale_bortle = ttk.Scale(form_container, from_=1, to=9, variable=self.bortle) # Escala Bortle vai de 1 a 9
        self.scale_bortle.grid(row=6, column=1, columnspan=2, sticky="ew", padx=5)
        self.spin_bortle = ttk.Spinbox(form_container, from_=1, to=8, textvariable=self.bortle, width=5)
        self.spin_bortle.grid(row=6, column=3, sticky="w")
        
        # --- Linha 8: Descrição ---
        ttk.Label(form_container, text="Descrição:").grid(row=7, column=0, sticky="nw", pady=(15, 5))
        self.entryDescricao = tk.Text(form_container, height=8, relief="solid", borderwidth=1)
        self.entryDescricao.grid(row=8, column=0, columnspan=4, sticky="nsew")

        # --- Área da Imagem (lado direito) ---
        ttk.Button(form_container, text="Adicionar imagem", command=self.upload_image).grid(row=0, column=4, sticky="ne", padx=10, pady=5)
        self.img_placeholder = tk.Frame(form_container, width=200, height=150, bg="white", relief="solid", borderwidth=1)
        self.img_placeholder.grid(row=1, column=4, rowspan=4, sticky="nsew", padx=10, pady=5)

        # --- Botão de Cadastrar (na parte de baixo) ---
        self.btn_cadastrar = ttk.Button(self.tela_anotacao, text="Cadastrar", command=self.salvar_registros)
        self.btn_cadastrar.pack(side="bottom", pady=(0, 10))

    def salvar_registros(self):
        print("Salvando")
        salvar_caminho_img = self.file_path
        salvar_astro = self.entryAstro.get()
        salvar_nomeregistro = self.entryNomeRegistro.get()
        salvar_data = self.entryData.get()
        salvar_horario = self.entryHorario.get()
        salvar_coordenadasX = self.entryCoordenadasX.get()
        salvar_coordenadasY = self.entryCoordenadasY.get()
        salvar_equipamento = self.entryEquipamento.get()
        salvar_visibilidade = self.visibilidade.get()
        salvar_escalabortle = self.bortle.get()
        salvar_descricao = self.entryDescricao.get("1.0", "end")
        self.controller.salvar_registro_controller(salvar_astro, salvar_nomeregistro, salvar_data, salvar_horario, salvar_coordenadasX, salvar_coordenadasY, salvar_equipamento, salvar_visibilidade, salvar_escalabortle, salvar_descricao, salvar_caminho_img)

        self.mostrar_tela_inicial()

    def upload_image(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        
if __name__ == "__main__":
    View()