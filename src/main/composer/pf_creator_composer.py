from src.models.settings.connection import db_connection_handler
from src.models.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pessoa_fisica_creator_controller import PessoaFisicaCreatorController
from src.views.pf_creator_view import PFCreatorView

def pf_creator_composer():
    model = PessoaFisicaRepository(db_connection_handler)
    controller = PessoaFisicaCreatorController(model)
    view = PFCreatorView(controller)

    return view
