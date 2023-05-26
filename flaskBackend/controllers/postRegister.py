import os
from flask import request
from models.characters import Character, db
from models.user import userSchema
import bcrypt
import jwt

# hash a password
def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'),  bcrypt.gensalt())
    return hashed_password.decode('utf-8')

# Generate a Jwt token
def generate_token(user_id):
    payload = {'user_id': user_id}
    secret_key = os.environ.get('JWT_SECRET_KEY')
    token = jwt.encode(payload, secret_key, algorithm='HS256')  
    return token


# for initially registering user
def register_user():
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        # hash the password
        hashed_password = hash_password(password)

        # create new user instance
        new_user = userSchema(email=email, password=hashed_password)

        # add new use to session and comit to database
        db.session.add(new_user)
        db.session.commit()

        # Generate a token for registered user
        token = generate_token(new_user.id)

        return {'meesage': 'User registered successfully', 'token': token }
    except Exception as e:
        return f"An error occured: {str(e)}"
    
def get_regis_user():
    try:

        #fetch all users from the database
        users = userSchema.query.all()

        # Extract the email values from users
        emails = [user.email for user in users]

        return {'emails': emails}
    except Exception as e:
        return {'error': str(e)}, 500