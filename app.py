from flask import Flask, request

app = Flask(__name__)

# This is supposed to be greet folder

@app.route('/')
def home_page():
    html = """
    <html>
        <body>
            <h1>Welcome to my home Page</h1>
            <p>This is the home page</p>
            <br>
            <a href='/welcome'>Welcome</a>
        </body>
    </html>
    """
    return html


@app.route('/welcome')
def welcome():
    html = """
    <html>
        <body>
            <h1>welcome</h1>
            <a href='/welcome/home'>Home</a>
            <br>
            <a href='/welcome/back'>Back</a>
        </body>
    </html>"""
    return html

@app.route('/welcome/home')
def welcome_home():
    return "welcome home"

@app.route('/welcome/back')
def back_home():
    return "welcome back"