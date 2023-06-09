from flask import Blueprint, jsonify, request
from models.characters import Character, db
from models.user import userSchema
from controllers.calculations import elo_rate_system
from controllers.postRegister import register_user, get_regis_user
from controllers.postLogin import login_user

routes_blueprint = Blueprint('routes', __name__)

# Define 'post' and 'get' routes
@routes_blueprint.route('/helloworld', methods={'GET'})
def resp():
    return "hello world"

# this is the get id for characters
@routes_blueprint.route('/characters/<int:id>', methods=['GET'])
def get_character(id):
    character = Character.query.get(id)

    if character:
        # Create a dictonary representing the character
        character_data = {
            # 'id': character.id,
            # 'name': character.name,
            'height': character.height,
            'weight': character.weight,
            'total_fights': character.total_fights,
            'wins': character.wins,
            'wins_by_ko': character.wins_by_ko,
            'draws': character.draws,
            'losses': character.losses,
            'stance': character.stance
        }

        return jsonify(character_data)
    else:
        return jsonify({'message': 'Character not found'}), 404
    
#define route for calculating matchup data.
@routes_blueprint.route('/characters/<int:id1>/<int:id2>', methods=['GET'])
def elo_rate_system_route(id1,id2):
    return elo_rate_system(id1,id2)

@routes_blueprint.route('/register', methods=['POST'])
def register_user_rout():
    return register_user()

@routes_blueprint.route('/register', methods=['GET'])
def get_regis_user_rout():
    return jsonify(get_regis_user())

@routes_blueprint.route('/login', methods=['POST'])
def login_user_rout():
    return login_user()