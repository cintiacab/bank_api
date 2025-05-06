from src.models.settings.connection import db_connection_handler
from src.models.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pessoa_fisica_withdrawer_controller import PFWithdrawerController
from src.views.pf_withdrawer_view import PFWithdrawerView

def pf_withdrawer_composer():
    model = PessoaFisicaRepository(db_connection_handler)
    controller = PFWithdrawerController(model)
    view = PFWithdrawerView(controller)

    return view
