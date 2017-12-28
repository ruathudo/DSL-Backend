from flask import request, jsonify
from app.api import api
from app.core import post


@api.route('/post', methods=['POST'])
def create():
    data = request.get_json()

    new_post, errs = post.create(uid=5, data=data)

    if errs:
        return jsonify({"Success": False, "error": errs})

    return jsonify({"Success": True, "data": new_post})


@api.route('/post/<string:slug>', methods=['GET'])
def get_by_slug(slug):

    post_data, errs = post.get_by_slug(slug)

    if errs:
        return jsonify({"Success": False, "error": errs})

    return jsonify({"Success": True, "data": post_data})


@api.route('/post/<int:pid>', methods=['GET'])
def get_by_id(pid):

    post_data, errs = post.get_by_id(pid)

    if errs:
        return jsonify({"Success": False, "error": errs})

    return jsonify({"Success": True, "data": post_data})


@api.route('/posts/<int:cid>', methods=['GET'])
def get_by_category(cid):

    post_data, errs = post.get_by_category(cid)

    if errs:
        return jsonify({"Success": False, "error": errs})

    return jsonify({"Success": True, "data": post_data})


@api.route('/post', methods=['PUT'])
def update():
    data = request.get_json()

    post_data, errs = post.update(data["id"], data)

    if errs:
        return jsonify({"Success": False, "error": errs})

    return jsonify({"Success": True, "data": post_data})


@api.route('/post', methods=['DELETE'])
def delete():
    data = request.get_json()

    post_data, errs = post.delete(data["id"])

    if errs:
        return jsonify({"Success": False, "error": errs})

    return jsonify({"Success": True, "data": post_data})
