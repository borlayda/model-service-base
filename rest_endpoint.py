from user_service.model import Model
from user_service.manager import ModelManager


class RestEndpoint():

    def __init__(self, model_manager: ModelManager):
        self.model_manager = model_manager

    def get(self, id: str = "", query: str = ""):
        return self.model_manager.get_by_id(id) if id else self.model_manager.get_by_query(query)

    def put(self, model: Model):
        self.model_manager.add(model)
        return model

    def post(self, model: Model):
        self.model_manager.update(model)
        return model

    def delete(self, id: str = "", query: str = ""):
        model = self.model_manager.get_by_id(id) if id else self.model_manager.get_by_query(query)
        if model is not None:
            self.model_manager.delete(model.id)
