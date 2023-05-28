import os
from flask import request
from models.characters import db
from models.user import userSchema
import jwt
import bcrypt

def login_user():
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        # print("Entered email:", email)

        user = db.session.query(userSchema).filter(userSchema.email == email).first()

        if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):

            # Generate JWT token
            secret_key = os.environ.get('JWT_SECRET_KEY')
            token = jwt.encode(
                {
                    'userId': user.id,
                    'email': user.email
                },
                secret_key,  # Replace with your token key
                algorithm='HS256'
            )

            return {
                'userDetails': {
                    'email': user.email,
                    'token': token,
                    '_id': user.id
                }
            }, 200

        # if user:
        #     print("Found user:", user) 
        # else:
        #     print("User not found") 
    
        return 'Invalid credentials. Please try again.', 400
    except Exception as e:
        return str(e), 500



