from flask import request, jsonify
from app.api import api
from app.core import category


@api.route("/category", methods=["POST"])
def create_category():
    data = request.get_json()

    category_data, errs = category.create(data["name"])

    if errs:
        return jsonify({"success": False, "error": errs})

    return jsonify({"success": True, "data": category_data})


@api.route("/categories", methods=["GET"])
def get_all_category():
    categories, errs = category.get()

    if errs:
        return jsonify({"success": False, "error": errs})

    return jsonify({"success": True, "data": categories})


@api.route("/category", methods=["PUT"])
def update_category():
    data = request.get_json()

    category_data, errs = category.update(data["id"], data["name"])

    if errs:
        return jsonify({"success": False, "error": errs})

    return jsonify({"success": True, "data": category_data})


@api.route("/category", methods=["DELETE"])
def delete_category():
    data = request.get_json()

    category_data, errs = category.delete(data["id"])

    if errs:
        return jsonify({"success": False, "error": errs})

    return jsonify({"success": True, "data": category_data})
