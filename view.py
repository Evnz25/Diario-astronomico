import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from controller import Controller
from PIL import Image, ImageTk

class View():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Diário Astronômico")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)
        self.file_path = None
        self.registro_atual_id = None

        self.controller = Controller(self)

        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.criar_tela_inicial()
        self.criar_tela_analise()
        self.criar_tela_anotacao()
        self.criar_tela_detalhes()
    
        self.mostrar_tela_inicial()

        self.root.mainloop()


    def mostrar_tela_inicial(self):
        self.atualizar_tela_inicial()
        self.tela_inicial.tkraise()
    
    def mostrar_tela_analise(self):
        self.atualizar_tela_analise()
        self.tela_analise_container.tkraise()

    def mostrar_tela_anotacao(self):
        self.tela_anotacao.tkraise()

    def mostrar_tela_detalhes(self, registro_id):
        self.registro_atual_id = registro_id
        registro = self.controller.pegar_registro_por_id_controller(registro_id)    
        if not registro:
            messagebox.showerror("Erro", "Não foi possível encontrar o registro pelo ID.")
            return
        
        self.detalhes_astro.config(text=registro.get('Astro', 'Astro não registrado'))
        self.detalhes_nome.config(text=registro.get('Nome', 'Nome não registrado'))
    
        data_obj = registro.get('Data')
        data_formatada = data_obj.strftime("%d/%m/%Y às %H:%M") if data_obj else "Data e horário não registrado"
        self.detalhes_data.config(text=data_formatada)

        self.detalhes_cidade.config(text=registro.get('Cidade', 'Cidade não registrado'))

        coords = f"X: {registro.get('CoordenadasX', ' Não registrado')} / Y: {registro.get('CoordenadasY', 'Não registrado')}"
        self.detalhes_coords.config(text=coords)

        self.detalhes_equip.config(text=registro.get('Equipamento', 'Equipamento não registrado'))
        self.detalhes_visib.config(text=str(registro.get('Visibilidade', 'Visibilidade não registrado')))
        self.detalhes_bortle.config(text=str(registro.get('EscalaBortle', 'Escala Bortle não registrado')))
        
        self.detalhes_desc.config(state='normal') 
        self.detalhes_desc.delete('1.0', 'end')
        self.detalhes_desc.insert('1.0', registro.get('Descricao', ''))
        self.detalhes_desc.config(state='disabled') 

        caminho_img = registro.get('Caminho_img')
        if caminho_img:
            try:
                img = Image.open(caminho_img)
                img.thumbnail((300, 250))
                photo = ImageTk.PhotoImage(img)
                self.detalhes_img_label.config(image=photo)
                self.detalhes_img_label.image = photo
            except FileNotFoundError:
                self.detalhes_img_label.config(image='', text="Imagem não encontrada")
        else:
            self.detalhes_img_label.config(image='', text="Sem imagem")

        self.tela_detalhes.tkraise()

    def atualizar_tela_inicial(self):
        for cartao in self.gallery_frame.winfo_children():
            cartao.destroy()

        registros = self.controller.pegar_todos_registros_controller()
        if not registros:
            ttk.Label(self.gallery_frame, text="Nenhuma anotação encontrada. Crie a primeira!", 
                      font=("Inter", 12), background="#F0F0F0").pack(pady=20)
            return

        for i, reg in enumerate(registros):
            linha = i // 4
            coluna = i % 4
            data_hora = f"{reg.get('Data', '')}"
            cartao = self._criar_cartao_anotacao(self.gallery_frame,
                                                 str(reg.get('_id')),
                                                 reg.get('Caminho_img', ''),
                                                 reg.get('Nome', 'Sem Título'),
                                                 data_hora)
            if cartao:
                cartao.grid(row=linha, column=coluna, padx=15, pady=15, sticky='n')

    def atualizar_tela_analise(self):
        num_registros = self.controller.qtd_registros_controller()
        astro_comum = self.controller.astro_mais_observado_controller()
        media_vis = self.controller.media_visibilidade_controller()
        mes_comum = self.controller.mes_de_mais_observacao_controller()
        mes_melhor_vis = self.controller.mes_de_melhor_visibilidade_controller()
        
        self.label_num_registros.config(text=f"Número de registros: {num_registros}")
        self.label_astro_comum.config(text=f"Astro mais observado: {astro_comum}")
        self.label_mes_comum.config(text=f"Mês de mais observação: {mes_comum}")
        self.label_media_vis.config(text=f"Visibilidade média: {media_vis}")
        self.label_mes_melhor_vis.config(text=f"Mês de melhor visibilidade: {mes_melhor_vis}")

        for cartao in self.melhor_anotacao_card_container.winfo_children(): 
            cartao.destroy()
        melhor_reg = self.controller.anotacao_melhor_visibilidade_controller()
        if melhor_reg:
            cartao = self._criar_cartao_anotacao(self.melhor_anotacao_card_container,
                                                 str(melhor_reg.get('_id')),
                                                 melhor_reg.get('Caminho_img', ''),
                                                 melhor_reg.get('Nome', 'Sem Título'),
                                                 melhor_reg.get('Data'))
            if cartao: cartao.pack(anchor='w')

    def criar_tela_inicial(self):
        self.tela_inicial = tk.Frame(self.container, bg="#F0F0F0")
        self.tela_inicial.grid(row=0, column=0, sticky='nsew')

        cabeçalho_frame = tk.Frame(self.tela_inicial, bg="#F0F0F0")
        cabeçalho_frame.pack(pady=20, padx=40, fill='x')
        
        ttk.Label(cabeçalho_frame, text="Diário Astronômico", font=("Inter", 28, "bold"), background="#F0F0F0").pack(anchor='w')
        
        botoes_frame = tk.Frame(cabeçalho_frame, bg="#F0F0F0")
        botoes_frame.pack(anchor='w', pady=15)
        
        ttk.Button(botoes_frame, text="Fazer registro", command=self.mostrar_tela_anotacao).pack(side="left")
        ttk.Button(botoes_frame, text="Ver análise", command=self.mostrar_tela_analise).pack(side="left", padx=10)

        tk.Frame(self.tela_inicial, height=10, bg="black").pack(fill='x')

        content_frame = tk.Frame(self.tela_inicial, bg="#F0F0F0")
        content_frame.pack(pady=20, padx=40, fill='both', expand=True)
        ttk.Label(content_frame, text="Anotações", font=("Inter", 22, "bold"), background="#F0F0F0").pack(anchor='w')
        
        canvas = tk.Canvas(content_frame, bg="#F0F0F0", highlightthickness=0)
        scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
        self.gallery_frame = tk.Frame(canvas, bg="#F0F0F0") 
        self.gallery_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.gallery_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def criar_tela_analise(self):
        self.tela_analise_container = tk.Frame(self.container, bg="#F0F0F0")
        self.tela_analise_container.grid(row=0, column=0, sticky='nsew')
        
        btn_voltar = ttk.Button(self.tela_analise_container, text="Voltar para o Início", style="Dark.TButton", command=self.mostrar_tela_inicial)
        btn_voltar.pack(side="bottom", pady=20)

        scroll_content_frame = tk.Frame(self.tela_analise_container, bg="#F0F0F0")
        scroll_content_frame.pack(fill="both", expand=True, padx=40, pady=(20, 0))

        canvas = tk.Canvas(scroll_content_frame, bg="#F0F0F0", highlightthickness=0)
        scrollbar = ttk.Scrollbar(scroll_content_frame, orient="vertical", command=canvas.yview)
        
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        
        scrollable_frame = tk.Frame(canvas, bg="#F0F0F0")
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True); scrollbar.pack(side="right", fill="y")
        
        card_dados_gerais = tk.Frame(scrollable_frame, bg="white", relief="solid", bd=1, highlightbackground="#D0D0D0", highlightthickness=1)
        card_dados_gerais.pack(pady=(20, 10), padx=40, fill='x')
        content_gerais = tk.Frame(card_dados_gerais, bg="white"); content_gerais.pack(padx=20, pady=15, anchor="w")
        ttk.Label(content_gerais, text="Dados gerais", font=("Inter", 14, "bold"), background="white").pack(anchor='w', pady=(0, 10))
        self.label_num_registros = ttk.Label(content_gerais, text="", font=("Inter", 11), background="white"); self.label_num_registros.pack(anchor='w')
        self.label_astro_comum = ttk.Label(content_gerais, text="", font=("Inter", 11), background="white"); self.label_astro_comum.pack(anchor='w')
        self.label_mes_comum = ttk.Label(content_gerais, text="", font=("Inter", 11), background="white"); self.label_mes_comum.pack(anchor='w')
        
        card_visibilidade = tk.Frame(scrollable_frame, bg="white", relief="solid", bd=1, highlightbackground="#D0D0D0", highlightthickness=1)
        card_visibilidade.pack(pady=10, padx=40, fill='x')
        content_visibilidade = tk.Frame(card_visibilidade, bg="white"); content_visibilidade.pack(padx=20, pady=15, anchor="w")
        ttk.Label(content_visibilidade, text="Visibilidade", font=("Inter", 14, "bold"), background="white").pack(anchor='w', pady=(0, 10))
        self.label_media_vis = ttk.Label(content_visibilidade, text="", font=("Inter", 11), background="white"); self.label_media_vis.pack(anchor='w')
        self.label_mes_melhor_vis = ttk.Label(content_visibilidade, text="", font=("Inter", 11), background="white"); self.label_mes_melhor_vis.pack(anchor='w', pady=(0, 5))

        card_bortle = tk.Frame(scrollable_frame, bg="white", relief="solid", bd=1, highlightbackground="#D0D0D0", highlightthickness=1)
        card_bortle.pack(pady=10, fill='x')
        content_bortle = tk.Frame(card_bortle, bg="white")
        content_bortle.pack(padx=20, pady=15, anchor="w", fill='x')

        input_frame = tk.Frame(content_bortle, bg="white")
        input_frame.pack(fill='x')
        
        ttk.Label(input_frame, text="Localizações pela escala Bortle:", font=("Inter", 11), background="white").pack(side="left", anchor='w')

        self.bortle_search_var = tk.IntVar(value=1)
        
        self.bortle_search_spinbox = ttk.Spinbox(
            input_frame, 
            from_=1, 
            to=9, 
            textvariable=self.bortle_search_var, 
            width=5,
            wrap=True 
        )
        self.bortle_search_spinbox.pack(side="left", padx=10)

        btn_buscar_bortle = ttk.Button(
            input_frame, 
            text="Buscar", 
            style="Dark.TButton", 
            command=self.buscar_cidades_por_bortle 
        )
        btn_buscar_bortle.pack(side="left")

        self.bortle_results_text = tk.Text(content_bortle, height=4, font=("Inter", 10), relief="solid", bd=1, wrap="word", bg="#F0F0F0")
        self.bortle_results_text.pack(fill='x', expand=True, pady=(10, 0))
        self.bortle_results_text.config(state='disabled') 


        melhor_anotacao_frame = tk.Frame(scrollable_frame, bg="#F0F0F0")
        melhor_anotacao_frame.pack(pady=(20, 10), padx=40, fill='x')
        ttk.Label(melhor_anotacao_frame, text="Anotação de melhor visibilidade", font=("Inter", 16, "bold"), background="#F0F0F0").pack(anchor='w', pady=(0, 10))
        self.melhor_anotacao_card_container = tk.Frame(melhor_anotacao_frame, bg="#F0F0F0")
        self.melhor_anotacao_card_container.pack(anchor="w")

    def criar_tela_anotacao(self):
        self.tela_anotacao = tk.Frame(self.container, bg="#E0E0E0")
        self.tela_anotacao.grid(row=0, column=0, sticky='nsew')
        form_container = ttk.Frame(self.tela_anotacao)
        form_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        form_container.grid_columnconfigure(1, weight=1)
        form_container.grid_rowconfigure(10, weight=1) 

        
        ttk.Label(form_container, text="Astros:").grid(row=0, column=0, sticky="w", pady=5)
        self.entryAstro = ttk.Entry(form_container)
        self.entryAstro.grid(row=0, column=1, columnspan=2, sticky="ew", padx=(5, 0))

        ttk.Label(form_container, text="Nome do registro:").grid(row=1, column=0, sticky="w", pady=5)
        self.entryNomeRegistro = ttk.Entry(form_container)
        self.entryNomeRegistro.grid(row=1, column=1, columnspan=2, sticky="ew", padx=(5, 0))
        
        data_frame = ttk.Frame(form_container)
        data_frame.grid(row=2, column=1, sticky="ew", padx=(5,0))
        
        ttk.Label(data_frame, text="Data:").pack(side="left", padx=(0,2))
        self.entryData = ttk.Entry(data_frame, width=10)
        self.entryData.pack(side="left")

        ttk.Label(form_container, text="Horário (HH:MM):").grid(row=3, column=0, sticky="w", pady=5)
        self.entryHorario = ttk.Entry(form_container, width=8)
        self.entryHorario.grid(row=3, column=1, sticky="w", padx=5)

        ttk.Label(form_container, text="Cidade:").grid(row=4, column=0, sticky="w", pady=5)
        self.entryCidade = ttk.Entry(form_container)
        self.entryCidade.grid(row=4, column=1, columnspan=2, sticky="ew", padx=(5, 0))

        ttk.Label(form_container, text="Coordenadas:").grid(row=5, column=0, sticky="w", pady=5)
        coord_frame = ttk.Frame(form_container)
        coord_frame.grid(row=5, column=1, sticky="w", padx=5)
        ttk.Label(coord_frame, text="X:").pack(side="left", padx=(0,2))
        self.entryCoordenadasX = ttk.Entry(coord_frame, width=15)
        self.entryCoordenadasX.pack(side="left")
        ttk.Label(coord_frame, text="Y:").pack(side="left", padx=(10,2))
        self.entryCoordenadasY = ttk.Entry(coord_frame, width=15)
        self.entryCoordenadasY.pack(side="left")
        
        ttk.Label(form_container, text="Equipamento:").grid(row=6, column=0, sticky="w", pady=5)
        self.entryEquipamento = ttk.Entry(form_container)
        self.entryEquipamento.grid(row=6, column=1, columnspan=2, sticky="ew", padx=(5, 0))

        ttk.Label(form_container, text="Visibilidade:").grid(row=7, column=0, sticky="w", pady=5)
        self.visibilidade = tk.IntVar(value=3)
        ttk.Scale(form_container, from_=1, to=5, variable=self.visibilidade).grid(row=7, column=1, sticky="ew", padx=5)
        ttk.Spinbox(form_container, from_=1, to=5, textvariable=self.visibilidade, width=5).grid(row=7, column=2, sticky="w")
        
        ttk.Label(form_container, text="Escala de Bortle:").grid(row=8, column=0, sticky="w", pady=5)
        self.bortle = tk.IntVar(value=5)
        ttk.Scale(form_container, from_=1, to=9, variable=self.bortle).grid(row=8, column=1, sticky="ew", padx=5)
        ttk.Spinbox(form_container, from_=1, to=9, textvariable=self.bortle, width=5).grid(row=8, column=2, sticky="w")
        
        ttk.Label(form_container, text="Descrição:").grid(row=9, column=0, sticky="nw", pady=(15, 5))
        self.entryDescricao = tk.Text(form_container, height=8, relief="solid", borderwidth=1)
        self.entryDescricao.grid(row=10, column=0, columnspan=3, sticky="nsew")

        image_frame = ttk.Frame(form_container)
        image_frame.grid(row=0, column=3, rowspan=11, sticky="n", padx=(20,0))
        ttk.Button(image_frame, text="Adicionar imagem", command=self.upload_image).pack()
        self.img_placeholder = tk.Frame(image_frame, width=200, height=150, bg="white", relief="solid", borderwidth=1)
        self.img_placeholder.pack(pady=5)

        btn_voltar = ttk.Button(self.tela_anotacao, text="Voltar para o Início", style="Dark.TButton", command=self.mostrar_tela_inicial)
        btn_voltar.pack(side="bottom", pady=20)

        self.btn_cadastrar = ttk.Button(self.tela_anotacao, text="Cadastrar", style="Dark.TButton", command=self.salvar_registros)
        self.btn_cadastrar.pack(side="bottom", pady=20)

    def criar_tela_detalhes(self):
        self.tela_detalhes = tk.Frame(self.container, bg="#E0E0E0")
        self.tela_detalhes.grid(row=0, column=0, sticky='nsew')

        btn_voltar = ttk.Button(self.tela_detalhes, text="Voltar para o Início", style="Dark.TButton", command=self.mostrar_tela_inicial)
        btn_voltar.pack(side="bottom", pady=20)

        btn_deletar = ttk.Button(self.tela_detalhes, text="Deletar Anotação", style="Dark.TButton", command=self.deletar_registro)
        btn_deletar.pack(side='bottom')

        details_container = tk.Frame(self.tela_detalhes, bg="#E0E0E0")
        details_container.pack(fill='both', expand=True, padx=20, pady=10)
        details_container.grid_columnconfigure(1, weight=1)

        self.detalhes_img_label = tk.Label(details_container, bg="white", relief="solid", bd=1)
        self.detalhes_img_label.grid(row=0, column=2, rowspan=6, sticky='n', padx=(20, 0))

        field_font = ("Inter", 11)
        label_font = ("Inter", 11, "bold")

        def criar_campo(row, label_text):
            ttk.Label(details_container, text=label_text, font=label_font, background="#E0E0E0").grid(row=row, column=0, sticky='w', pady=4)
            data_label = ttk.Label(details_container, text="", font=field_font, background="#E0E0E0", wraplength=400)
            data_label.grid(row=row, column=1, sticky='w', padx=10)
            return data_label

        self.detalhes_astro = criar_campo(0, "Astros:")
        self.detalhes_nome = criar_campo(1, "Nome do registro:")
        self.detalhes_data = criar_campo(2, "Data e Horário:")
        self.detalhes_cidade = criar_campo(3, "Cidade:")
        self.detalhes_coords = criar_campo(4, "Coordenadas:")
        self.detalhes_equip = criar_campo(5, "Equipamento:")
        self.detalhes_visib = criar_campo(6, "Visibilidade:")
        self.detalhes_bortle = criar_campo(7, "Escala de Bortle:")

        ttk.Label(details_container, text="Descrição:", font=label_font, background="#E0E0E0").grid(row=7, column=0, sticky='nw', pady=4)
        self.detalhes_desc = tk.Text(details_container, height=8, font=field_font, relief="solid", bd=1, wrap="word")
        self.detalhes_desc.grid(row=8, column=0, columnspan=3, sticky='nsew', pady=(0, 10))
        self.detalhes_desc.config(state='disabled')

    def salvar_registros(self):
        if not self.file_path:
            messagebox.showwarning("Aviso", "Por favor, adicione uma imagem para o registro.")
            return

        dados = {
            'astro': self.entryAstro.get(),
            'nome': self.entryNomeRegistro.get(),
            'data': self.entryData.get(),
            'horario': self.entryHorario.get(),
            'cidade': self.entryCidade.get(),
            'coord_x': self.entryCoordenadasX.get(),
            'coord_y': self.entryCoordenadasY.get(),
            'equipamento': self.entryEquipamento.get(),
            'visibilidade': self.visibilidade.get(),
            'bortle': self.bortle.get(),
            'descricao': self.entryDescricao.get("1.0", "end-1c"),
            'imagem_path': self.file_path
        }
        
        if not dados['nome']:
            messagebox.showerror("Erro de Validação", "O campo 'Nome do registro' é obrigatório.")
            return

        sucesso = self.controller.salvar_registro_controller(
            dados['astro'], dados['nome'], dados['data'], dados['horario'], dados['cidade'],
            dados['coord_x'], dados['coord_y'], dados['equipamento'],
            dados['visibilidade'], dados['bortle'], dados['descricao'], dados['imagem_path']
        )

        if sucesso:
            messagebox.showinfo("Sucesso", "Registro salvo com sucesso!")
            self.entryAstro.delete(0, 'end')
            self.entryNomeRegistro.delete(0, 'end')
            self.entryData.delete(0, 'end')
            self.entryHorario.delete(0, 'end')
            self.entryCidade.delete(0, 'end')
            self.entryCoordenadasX.delete(0, 'end')
            self.entryCoordenadasY.delete(0, 'end')
            self.entryEquipamento.delete(0, 'end')
            self.entryDescricao.delete('1.0', 'end')
            self.visibilidade.set(3); self.bortle.set(5)
            self.file_path = None
            for widget in self.img_placeholder.winfo_children(): widget.destroy()

            self.mostrar_tela_inicial()
        else:
            messagebox.showerror("Erro no Banco de Dados", "Não foi possível salvar o registro.")

    def upload_image(self):        
        path = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg *.jpeg *.png *.gif")])
        if path:
            self.file_path = path
            for widget in self.img_placeholder.winfo_children():
                widget.destroy()
            
            img = Image.open(self.file_path)
            img.thumbnail((200, 150))
            photo = ImageTk.PhotoImage(img)
            
            img_label = tk.Label(self.img_placeholder, image=photo, bg="white")
            img_label.image = photo
            img_label.pack()

    def _criar_cartao_anotacao(self, parent, registro_id, imagem_path, titulo, data_obj):
        card_frame = tk.Frame(parent, bg="#F0F0F0", cursor="hand2") # Adiciona cursor de "mãozinha"
      
        if imagem_path:
            try:
                img = Image.open(imagem_path)
                img.thumbnail((200, 150))
                photo = ImageTk.PhotoImage(img)
                label_imagem = tk.Label(card_frame, image=photo, borderwidth=0)
                label_imagem.image = photo
                label_imagem.pack(pady=(0, 10))
            except Exception:
                placeholder = tk.Frame(card_frame, width=200, height=150, bg="grey")
                placeholder.pack(pady=(0, 10))
        else:
            placeholder = tk.Frame(card_frame, width=200, height=150, bg="grey")
            placeholder.pack(pady=(0, 10))
        
        label_titulo = ttk.Label(card_frame, text=titulo, font=("Inter", 12, "bold"), background="#F0F0F0")
        label_titulo.pack(anchor='w')

        label_data = ttk.Label(card_frame, text=data_obj, font=("Inter", 9), background="#F0F0F0", foreground="#555555")
        label_data.pack(anchor='w')

        on_click = lambda event, reg_id=registro_id: self.mostrar_tela_detalhes(reg_id)

        card_frame.bind("<Button-1>", on_click)
        for widget in card_frame.winfo_children():
            widget.bind("<Button-1>", on_click)

        return card_frame
    
    def deletar_registro(self):
        sucesso = self.controller.deletar_registro_controller(self.registro_atual_id)

        if sucesso:
            messagebox.showinfo("Sucesso", "Anotação deletada com sucesso.")
            self.registro_atual_id = None
            self.mostrar_tela_inicial()
        else:
            messagebox.showerror("Erro", "Não foi possível deletar a anotação.")

    def buscar_cidades_por_bortle(self):
        valor_bortle = self.bortle_search_var.get()
        
        lista_cidades = self.controller.pegar_cidades_por_bortle_controller(valor_bortle)
        
        if lista_cidades:
            resultado_str = ", ".join(lista_cidades)
        else:
            resultado_str = f"Nenhuma cidade encontrada com escala Bortle {int(valor_bortle)}."
            
        self.bortle_results_text.config(state='normal')    
        self.bortle_results_text.delete('1.0', 'end')      
        self.bortle_results_text.insert('1.0', resultado_str) 
        self.bortle_results_text.config(state='disabled')  

if __name__ == "__main__":
    app = View()