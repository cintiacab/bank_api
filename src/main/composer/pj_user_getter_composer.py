from src.models.settings.connection import db_connection_handler
from src.models.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.pessoa_juridica_user_getter_controller import PJGetUsersController
from src.views.pj_user_getter_view import PJGetUsersView

def pj_user_getter_composer():
    model = PessoaJuridicaRepository(db_connection_handler)
    controller = PJGetUsersController(model)
    view = PJGetUsersView(controller)

    return view
