from flask import Flask, request

app = Flask(__name__)

#App routing is used to map the specific URL with the associated function that is intended to perform some task.
#the URL ('/') is associated with the Hello_World function.
@app.route('/')
def Hello_World():
    return '<h1>Hello! This is my first website.<h1>'

if __name__ == '__main__':
    app.run()
