from src.models.settings.connection import db_connection_handler
from src.models.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pessoa_fisica_statement_shower_controller import PFStatementShowerController
from src.views.pf_statement_shower_view import PFStatementShowerView

def pf_statement_shower_composer():
    model = PessoaFisicaRepository(db_connection_handler)
    controller = PFStatementShowerController(model)
    view = PFStatementShowerView(controller)

    return view
