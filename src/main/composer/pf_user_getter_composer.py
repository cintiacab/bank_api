from src.models.settings.connection import db_connection_handler
from src.models.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pessoa_fisica_user_getter_controller import PFGetUsersController
from src.views.pf_user_getter_view import PFGetUsersView

def pf_user_getter_composer():
    model = PessoaFisicaRepository(db_connection_handler)
    controller = PFGetUsersController(model)
    view = PFGetUsersView(controller)

    return view
