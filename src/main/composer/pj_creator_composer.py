from src.models.settings.connection import db_connection_handler
from src.models.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.pessoa_juridica_creator_controller import PessoaJuridicaCreatorController
from src.views.pj_creator_view import PJCreatorView

def pj_creator_composer():
    model = PessoaJuridicaRepository(db_connection_handler)
    controller = PessoaJuridicaCreatorController(model)
    view = PJCreatorView(controller)

    return view
