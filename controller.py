from model import Model

class Controller():
    def __init__(self, view):
        self.model = Model()
        
        self.view = view

    def salvar_registro_controller(self, salvar_astro,  salvar_data, salvar_nomeregistro, salvar_horario, salvar_cidade, salvar_coordenadasX, salvar_coordenadasY, salvar_equipamento, salvar_visibilidade, salvar_escalabortle, salvar_descricao, salvar_caminho_img):
        return self.model.salvar_registro(salvar_astro,  salvar_data, salvar_nomeregistro, salvar_horario, salvar_cidade, salvar_coordenadasX, salvar_coordenadasY, salvar_equipamento, salvar_visibilidade, salvar_escalabortle, salvar_descricao, salvar_caminho_img)
        
    def qtd_registros_controller(self):
        text = self.model.qtd_registros()
        return(text)

    def astro_mais_observado_controller(self):
        text = self.model.astro_mais_observado()
        return(text)

    def media_visibilidade_controller(self):
        text = self.model.media_visibilidade()
        return(text)

    def pegar_todos_registros_controller(self):
        return self.model.pegar_registros()
    
    def mes_de_mais_observacao_controller(self):
        return self.model.mes_de_mais_observacao()
    
    def mes_de_melhor_visibilidade_controller(self):
        return self.model.mes_de_melhor_visibilidade()

    def anotacao_melhor_visibilidade_controller(self):
        return self.model.anotacao_melhor_visibilidade()
    
    def pegar_registro_por_id_controller(self, registro_id):
        return self.model.pegar_registro_por_id(registro_id)
    
    def deletar_registro_controller(self, registro_id):
        return self.model.deletar_registro(registro_id)
    
    def pegar_cidades_por_bortle_controller(self, bortle_valor):
        return self.model.pegar_cidades_por_bortle(bortle_valor)
        