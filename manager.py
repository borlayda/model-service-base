from user_service.model import Model


class ModelManager():

    def __init__(self, model: Model):
        self.definition = model.__dict__
