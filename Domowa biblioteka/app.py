from flask import Flask, jsonify
from models import towatches
from flask import abort
from flask import make_response
from flask import request

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/api/v1/towatches/", methods=["GET"])
def towatches_list_api_v1():
    return jsonify(towatches.all())

@app.route("/api/v1/towatches/<int:towatch_id>", methods=["GET"])
def get_towatch(towatch_id):
    towatch = towatches.get(towatch_id)
    if not towatch:
        abort(404)
    return jsonify({"towatch": towatch})


@app.route("/api/v1/towatches/", methods=["POST"])
def create_towatch():
    if not request.json or not 'title' in request.json:
        abort(400)
    towatch = {
        'id': towatches.all()[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    towatches.create(towatch)
    return jsonify({'towatch': towatch}), 201

@app.route("/api/v1/towatches/<int:towatch_id>", methods=['DELETE'])
def delete_towatch(towatch_id):
    result = towatches.delete(towatch_id)
    if not result:
        abort(404)
    return jsonify({'result': result})

@app.route("/api/v1/towatches/<int:towatch_id>", methods=["PUT"])
def update_towatch(towatch_id):
    towatch = towatches.get(towatch_id)
    if not towatch:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'description' in data and not isinstance(data.get('description'), str),
        'done' in data and not isinstance(data.get('done'), bool)
    ]):
        abort(400)
    towatch = {
        'title': data.get('title', towatch['title']),
        'description': data.get('description', towatch['description']),
        'done': data.get('done', towatch['done'])
    }
    towatches.update(towatch_id, towatch)
    return jsonify({'towatch': towatch})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)

if __name__ == "__main__":
    app.run(debug=True)
