from . import api
from ..exceptions import ValidationError
from flask import jsonify



@api.errorhandler(404)
def page_not_found(error):
    response = {
        "error": "Page not found",
        "message": "The requested URL was not found on the server."
    }
    return jsonify(response), 404

@api.errorhandler(404)
def page_not_found(error):
    response = {
        "error": "Page not found",
        "message": "The requested URL was not found on the server."
    }
    return jsonify(response), 404


@api.errorhandler(500)
def internal_server_error(error):
    response = {
        "error": "Internal Server Error",
        "message": "An unexpected error occurred on the server."
    }
    return jsonify(response), 500


@api.errorhandler(501)
def not_implemented(error):
    response = {
        "error": "Not Implemented",
        "message": "The server does not support the functionality required to fulfill the request."
    }
    return jsonify(response), 501



@api.errorhandler(ValidationError)
def handle_validation_error(error):
    response = {
        "error": "Validation Error",
        "message": str(error)
    }
    return jsonify(response), 400 
