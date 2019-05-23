from flask import jsonify


def return_response(message, status_code):
    response = jsonify(message)
    response.status_code = status_code
    return response
