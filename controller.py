from model import Model

class Controller():
    def __init__(self, view):
        self.model = Model()
        
        self.view = view
        
    def qtd_registros_controller(self):
        text = self.model.qtd_registros()
        self.view.update_view(str(text))
        