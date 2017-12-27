from flask import jsonify

from . import api


@api.route('/post', methods=['GET'])
def get_post():

    return jsonify({"success": True})
