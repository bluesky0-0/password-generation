from flask import Flask, request, jsonify, render_template
import random
import string

app = Flask(__name__)

def genpasswd(length=10):
    if length < 4:
        raise ValueError('password length too short')
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    special = string.punctuation
    password = [
        random.choice(lowercase), random.choice(uppercase),
        random.choice(numbers), random.choice(special)
    ]

    characters = lowercase + uppercase + numbers + special
    password += random.choices(characters, k=length-4)
    random.shuffle(password)
    return ''.join(password)


@app.route('/generate')

def generate():
    length = request.args.get('length', default=10)
    try:
        length = int(length)
        if length < 4:
            return jsonify(error="Password must be at least 4 characters."), 400
    except ValueError:
        return jsonify(error="Invalid length"), 400
    password = genpasswd(length)
    return jsonify(password=password)

if __name__ =='__main__':
    app.run(debug=True)

