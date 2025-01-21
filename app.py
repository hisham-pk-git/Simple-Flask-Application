from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Static JSON data
users = {
    "users": [
        {"id": 1, "username": "john_doe", "email": "john@example.com"},
        {"id": 2, "username": "Hisham Panamthodi Kajahussain", "email": "hisham.pk@csu.fullerton.edu"},
        {"id": 3, "username": "alice_jones", "email": "alice@example.com"}
    ]
}

@app.route('/')
def homepage():
    return render_template('index.html', users=users['users'])

@app.route('/user/<int:user_id>')
def user_detail(user_id):
    user = next((u for u in users['users'] if u['id'] == user_id), None)
    if user:
        return jsonify({"username": user['username'], "email": user['email']})
    else:
        return "User not found", 404
    


if __name__ == '__main__':
    app.run(debug=True)
