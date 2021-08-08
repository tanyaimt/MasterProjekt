from flask import Flask
from flask.json import jsonify, request
from departments import departments

app = Flask(__name__)

@app.route('/health')
def health():
    return "Pong"


@app.route('/healthjson')
def healthjson():
    return jsonify({"message": "Pong"})


@app.route('/departments')
def getDepartments():
    return jsonify(departments)

@app.route('/departments/<string:Description>')
def getDepartment(Description):
    departmentFound = [department for department in departments if department['Description']==Description]
    if len(departmentFound) < 1:
        return (Description+" Department not found")
    return jsonify({"Department":departmentFound[0]})

@app.route('/departments', methods=['POST'])
def postDepartment():
    new_department ={
        "Description": request.json['Description'],
        "Manager": request.json['Manager']
    }
    departments.append(new_department)
    return jsonify({"Message":"New Dep Added", "departments": departments})


@app.route('/departments/<string:Description>', methods=['PUT'])
def putDepartment(Description):
    departmentFound = [department for department in departments if department['Description']==Description]
    if len(departmentFound) > 0:
        departmentFound[0]['Description'] = request.json['Description']
        departmentFound[0]['Manager'] = request.json['Manager']
    return jsonify({"Message":"Dep Modify", "departments": departments})


@app.route('/departments/<string:Description>', methods=['DELETE'])
def deleteDepartment(Description):
    departmentFound = [department for department in departments if department['Description']==Description]
    if len(departmentFound) > 0:
        departments.remove(departmentFound[0])
        return jsonify({"Message":"Dep Deleted", "departments": departments})
    return jsonify({"Message":"Product not found", "departments": departments})


if __name__ == '__main__':
    app.run(debug=True, port=4001) 