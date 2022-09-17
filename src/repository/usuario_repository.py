from src.repository.context.api_context import ApiContext

class user_repository(object):
    _apiContext: ApiContext = ApiContext()

    def __init__(self) -> None:
        pass

    def get(self):
        return self._apiContext.user_table.get_all()

    def busca_id_usuario(self,id):
        return self._apiContext.user_table.get(id)

    def post_usuario(self, objectPost):
        self._apiContext.user_table.begin_transaction()
        self._apiContext.user_table.insert(objectPost)
        self._apiContext.user_table.commit()

