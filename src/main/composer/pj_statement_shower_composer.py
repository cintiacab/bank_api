from src.models.settings.connection import db_connection_handler
from src.models.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.pessoa_juridica_statement_shower_controller import PJStatementShowerController
from src.views.pj_statement_shower_view import PJStatementShowerView

def pj_statement_shower_composer():
    model = PessoaJuridicaRepository(db_connection_handler)
    controller = PJStatementShowerController(model)
    view = PJStatementShowerView(controller)

    return view
