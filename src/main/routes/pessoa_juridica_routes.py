from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.main.composer.pj_creator_composer import pj_creator_composer
from src.main.composer.pj_user_getter_composer import pj_user_getter_composer
from src.main.composer.pj_statement_shower_composer import pj_statement_shower_composer
from src.main.composer.pj_withdrawer_composer import pj_withdrawer_composer
from src.errors.error_handler import handle_errors

pj_route_bp = Blueprint("pj_routes", __name__)

@pj_route_bp.route("/pessoa_juridica/create", methods=["POST"])
def create_user():
    try:
        http_request = HttpRequest(body= request.json)
        view = pj_creator_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@pj_route_bp.route("/pessoa_juridica/list", methods=["GET"])
def get_users():
    try:
        http_request = HttpRequest()
        view = pj_user_getter_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@pj_route_bp.route("/pessoa_juridica/statement/<user_id>", methods=["GET"])
def show_statement(user_id):
    try:
        http_request = HttpRequest(param = {"user_id" : user_id})
        view = pj_statement_shower_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@pj_route_bp.route("/pessoa_juridica/withdraw/<user_id>", methods=["PATCH"])
def withdraw_account(user_id):
    try:
        http_request = HttpRequest(body= request.json, param = {"user_id" : user_id})
        view = pj_withdrawer_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
