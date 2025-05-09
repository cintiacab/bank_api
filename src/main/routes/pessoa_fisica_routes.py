from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.main.composer.pf_creator_composer import pf_creator_composer
from src.main.composer.pf_user_getter_composer import pf_user_getter_composer
from src.main.composer.pf_statement_shower_composer import pf_statement_shower_composer
from src.main.composer.pf_withdrawer_composer import pf_withdrawer_composer
from src.errors.error_handler import handle_errors

pf_route_bp = Blueprint("pf_routes", __name__)

@pf_route_bp.route("/pessoa_fisica/create", methods=["POST"])
def create_user():
    try:
        http_request = HttpRequest(body= request.json)
        view = pf_creator_composer()
        
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@pf_route_bp.route("/pessoa_fisica/list", methods=["GET"])
def get_users():
    try:
        http_request = HttpRequest()
        view = pf_user_getter_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@pf_route_bp.route("/pessoa_fisica/statement/<user_id>", methods=["GET"])
def show_statement(user_id):
    try:
        http_request = HttpRequest(param = {"user_id" : user_id})
        view = pf_statement_shower_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@pf_route_bp.route("/pessoa_fisica/withdraw/<user_id>", methods=["PATCH"])
def withdraw_account(user_id):
    try:
        http_request = HttpRequest(body= request.json, param = {"user_id" : user_id})
        view = pf_withdrawer_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
            http_response = handle_errors(exception)
            return jsonify(http_response.body), http_response.status_code
