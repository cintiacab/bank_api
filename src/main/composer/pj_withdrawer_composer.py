from src.models.settings.connection import db_connection_handler
from src.models.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.pessoa_juridica_withdrawer_controller import PJWithdrawerController
from src.views.pj_withdrawer_view import PJWithdrawerView

def pj_withdrawer_composer():
    model = PessoaJuridicaRepository(db_connection_handler)
    controller = PJWithdrawerController(model)
    view = PJWithdrawerView(controller)

    return view
