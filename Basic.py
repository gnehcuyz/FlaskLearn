from crypt import methods
from unicodedata import name
from flask import Flask, request, json, jsonify, session, redirect, url_for, render_template
from flask_cors import CORS, cross_origin
import flask
flask.__version__
app = Flask(__name__)



@app.route('/guard')
def guard(method=['GET']):
        if 'username' in session:
                return jsonify('{"auth": "1"}')
        else:
                return jsonify('{"auth": "0"}')

@app.route('/admin')
def index():
        return redirect(url_for('login'))

# @app.route('/login/rpi', methods=["POST", "GET"])
# def login():
#         #print(next)
#         ticket = request.args.get('ticket')
#         if not ticket:
#                 print(cas.get_login_url())
#                 return redirect(cas.get_login_url())

#         print(ticket)
#         user, attributes, pgtiou = cas.verify_ticket(ticket)

#         if not user:
#                 return "Failed to Verify Login Ticket"
#         else:
#                 session['username'] = user
#                 return redirect("https://hasspathways.com/admin-portal")



@app.route("/edit", methods=["POST", "GET"]) # POST
def editAdmin():
        response = {'status':'success'}
        if request.method == "POST":
                dat = request.get_json()
                name = dat.get('courses'),
                pathways = dat.get('pathways')
                print(name)
                print(pathways)

                response['message'] = 'Success!'

        return jsonify(response)

@app.route('/test', methods=["GET"]) # GET
                                    # <-- this an endpoint header, endpoints run functions
def test():
        return render_template("admin.html")



# difference between GET and POST as well as how they work
# how you create endpoints -> what that means
# how flask uses python dictionaries to process data


# Create a basic API in flask, which has the following endpoints:


# /dashboard -> GET
@app.route("/dashboard", methods=["GET"])
def dashboard():
        return render_template("dashboard.html")


# display data in a json format containing the following:
#       1. number of commits you have
#       2. your name
#       3. your grad (projected) year

# /input -> POST
@app.route("/getInput", methods=["POST", "GET"])
def getInput():
        response = {'status':'success'}
        if request.method == "POST":
                dat = request.get_json()
                name = dat.get('name'),
                gradYear = dat.get('gradYear')
                print(name)
                print(gradYear)
        return jsonify(response)

# display the arguments given in a POST request to this endpoint
# -> package as dictionary with key being key from post, value being value

# POST
# -> {"name": "hi", "age": "43"}
# your function will print
# -> name: hi
# -> age: 43
@app.route("/getPost", methods=["POST"])
def getPost():
        response = {'status':'success'}
        if request.method == "POST":
                dat = request.get_json()
                name = dat.get('name'),
                age = dat.get('age')
                print(name)
                print(age)
        return jsonify(response)

# highly suggest using postman to test your endpoints
# https://www.postman.com/
# use postman to call post requests to your API while its running
# for example: http//09.0.0./input

if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True)