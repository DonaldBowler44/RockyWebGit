from flask import Blueprint, jsonify
from models.characters import Character
from controllers.calculations import elo_rate_system

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
