from flask import jsonify
from models.characters import Character

def elo_rate_system(id1, id2):
    characterOne = Character.query.get(id1)
    characterTwo = Character.query.get(id2)

    ratingOne = 0 # Initialize ratingOne variable
    ratingTwo = 0 # Initialize ratingTwo variable

    S_A = 0
    S_B = 0

    upd_ratingOne = 0
    upd_ratingTwo = 0
    K = 16

    characters_data = {}

    if characterOne:
        if id1 == 1:
            characters_data['characterOne'] = characterOne.name
            ratingOne = 2850
        if id1 == 2:
             characters_data['characterOne'] = characterOne.name
             ratingOne = 2750 
        if id1 == 3:
             characters_data['characterOne'] =  characterOne.name
             ratingOne = 2820 
        if id1 == 4:
             characters_data['characterOne'] = characterOne.name
             ratingOne = 2550 
        if id1 == 5:
             characters_data['characterOne'] = characterOne.name
             ratingOne = 2200 
        if id1 == 6:
              characters_data['characterOne'] = characterOne.name
              ratingOne = 2500 
        if id1 == 7:
              characters_data['characterOne'] = characterOne.name
              ratingOne = 2650 
        if id1 == 8:
              characters_data['characterOne'] = characterOne.name
              ratingOne = 2400  
        if id1 == 9:
              characters_data['characterOne'] = characterOne.name
              ratingOne = 2490   
        if id1 == 10:
              characters_data['characterOne'] = characterOne.name
              ratingOne = 2610  
        if id1 == 11:
              characters_data['characterOne'] = characterOne.name
              ratingOne = 2480  
        
    if characterTwo:
        if id2 == 1:
              characters_data['characterTwo'] = characterTwo.name
              ratingTwo = 2850 
        if id2 == 2:
              characters_data['characterTwo'] = characterTwo.name
              ratingTwo = 2750 
        if id2 == 3:
              characters_data['characterTwo'] = characterTwo.name
              ratingTwo = 2820 
        if id2 == 4:
              characters_data['characterTwo'] = characterTwo.name
              ratingTwo = 2550 
        if id2 == 5:
              characters_data['characterTwo'] = characterTwo.name
              ratingTwo = 2200 
        if id2 == 6:
              characters_data['characterTwo'] = characterTwo.name
              ratingTwo = 2500 
        if id2 == 7:
              characters_data['characterTwo'] = characterTwo.name
              ratingTwo = 2650 
        if id2 == 8:
              characters_data['characterTwo'] = characterTwo.name
              ratingTwo = 2400 
        if id2 == 9:
              characters_data['characterTwo'] = characterTwo.name
              ratingTwo = 2490 
        if id2 == 10:
              characters_data['characterTwo'] = characterTwo.name
              ratingTwo = 2610 
        if id2 == 11:
              characters_data['characterTwo'] = characterTwo.name
              ratingTwo = 2480 
        
        # elo rating algorithm for probability  
        E_A = 1 / (1 + 10 ** ((ratingTwo - ratingOne) / 400))
        E_B = 1 / (1 + 10 ** ((ratingOne - ratingTwo) / 400))

        characters_data['characterOne_E_A_Value'] = E_A
        characters_data['characterTwo_E_B_Value'] = E_B

        if E_A >= E_B:
              S_A = 1
        else:
              S_A = 0

        if E_B >= E_A:
              S_B = 1
        else:
              S_B = 0

      #update rating based on elo rate system
        upd_ratingOne = ratingOne + (K *(S_A -E_A ))
        upd_ratingTwo = ratingTwo + (K *(S_B - E_B))

        characters_data['characterOne_upR_A_Value'] = upd_ratingOne
        characters_data['characterTwo_upR_B_Value'] = upd_ratingTwo  

        return jsonify(characters_data)
     