from dataclasses import asdict
from functools import partial

from flask import Blueprint, request, jsonify
from jinja2.lexer import Failure
from returns.maybe import Nothing
from returns.result import Success

from repository.target_repository import find_target_by_id, find_all_target
from services.target_service import convert_to_json

target_blueprint = Blueprint("target", __name__)

@target_blueprint.route("/<int:target_id>", methods=['GET'])
def get_target_by_id(target_id):
    return (
        find_target_by_id(target_id)
        .map(convert_to_json)
        .map(lambda u: (jsonify(u), 200))
        .value_or((jsonify({}), 400))
    )

@target_blueprint.route("/all", methods=['GET'])
def get_target():
    return (
        find_all_target()
        .map(lambda targets: [convert_to_json(target) for target in targets])
        .map(lambda u: (jsonify(u), 200))
        .value_or((jsonify({}), 404))
    )
