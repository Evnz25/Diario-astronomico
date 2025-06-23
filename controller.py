from model import Model

class Controller():
    def __init__(self, view):
        self.model = Model()
        
        self.view = view

    def salvar_registro_controller(self, salvar_astro, salvar_nomeregistro, salvar_data, salvar_horario, salvar_coordenadasX, salvar_coordenasY, salvar_equipamento, salvar_visibilidade, salvar_escalabortle, salvar_descricao, salvar_caminho_img):
        self.model.salvar_registro(salvar_astro, salvar_nomeregistro, salvar_data, salvar_horario, salvar_coordenadasX, salvar_coordenasY, salvar_equipamento, salvar_visibilidade, salvar_escalabortle, salvar_descricao, salvar_caminho_img)
        
    def qtd_registros_controller(self):
        text = self.model.qtd_registros()
        self.view.update_view(str(text))

    def astro_mais_observado_controller(self):
        text = self.model.astro_mais_observado()
        self.view.update_view(str(text))

    def media_visibilidade_controller(self):
        text = self.model.media_visibilidade()
        self.view.update_view(str(text))
        