from flask import Flask,jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'name': 'Jaislin',
        'role': 'Junior Software Engineer', 
        'age': 21
    },
    {
        'id': 2,
        'name': 'Indus',
        'role': 'Junior Software Engineer', 
        'Age': 22
    }
]

@app.route("/")
def hello_world():
    return "Welcome to my world"
 #Post method
@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })

#GET method
@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)