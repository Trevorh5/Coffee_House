import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

# db_drop_and_create_all()

## ROUTES

@app.route('/drinks', methods=['GET'])
def get_drinks():
    drinks = [drink.short() for drink in Drink.query.all()]
    return jsonify({'success': True, 'drinks': drinks})

@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drinks_detail(arg):
    drinks = [drink.long() for drink in Drink.query.all()]
    return jsonify({'success': True, 'drinks': drinks})


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def create_drink(arg):
    title = request.json.get('title')
    recipe = request.json.get('recipe')

    new_drink = Drink(title = title, recipe = json.dumps(recipe))
    new_drink.insert()

    return jsonify({
        'success': True,
        'drinks': [new_drink.long()]
    })


@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def edit_drink(jwt, id):
    drink = Drink.query.filter(Drink.id == id).one_or_none()

    title = request.json.get('title')
    recipe = request.json.get('recipe')

    if drink: 
        drink.title = title
        drink.recipe = json.dumps(recipe)
        drink.update()
        return jsonify({'success': True, 'drinks': [drink.long()] })
    else:
        abort(404)


@app.route('/drinks/<int:id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(jwt, id):
    drink = Drink.query.filter(Drink.id == id).one_or_none()

    if drink: 
        drink.delete()
        return jsonify({
            "success": True,
            "delete": id
        })
    else:
        abort(404)



## Error Handling

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False, 
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "Not found"
    }), 404


@app.errorhandler(AuthError)
def auth_error(e):
    return jsonify({
        "success": False,
        "error": e.error['code'],
        "message": e.error['description']
    }), e.status_code