Unit 23.1 of the Software Engineering Foundations Certificate Program at Stony Brook University
- This chapter introduced us to Flask.
- Flask is a popular backend web framework that works alongside Python

____________________________________________________
Creating a virtual enviornment:
- In Terminal do the following:
    - python3 -m venv venv
        - This will create a virtual environment inside the venv folder
        - The virtual environment is to perform testing without possibly interfering with your own PC files.
    - source venv/bin/activate
        - The notes required venv/scripts/activate. This never worked for me. A scripts file was never created.
        - This will open your Terminal inside the virtual enviornment
        - You will see (venv) as the first note in your command line
    - (venv) $ pip3 install flask
        - will install flask
    - (venv) $pip3 freeze > requirements.txt
        - This will create a txt file of requirements necessary to run the code, everything that is downloaded in the virtual enviornment
        - You can read the code by typing:
            - cat requirements.txt

_______________________________________________
To setup files:
- The following line must be at the top of any Python file
    - from flask import Flask, request
    - app = Flask(__name__)
        - __name__ should be untouched and written exactly as is
    - flask run
        - Will run the app.py file
        - If the file is not called app.py use:
            - FLASK_APP=nameOfFile.py flask run
        - Using flask run will provide a local host address. This is where you can open created routes

_______________________________________________
Greet
- Contains a few route files to go to
    - /welcome
    - /welcome/home
    - /welcome/back
- You can also do python3 -m unittest test.py to run the unit test

_______________________________________________
Calc
- The routes for Calc are a bit more complicated because there is no landing page
- The program functions as a calculator. The operations are taken from operations.py and then imported into app.py
- /add is a route
    - Nothing will come up with localhost:5000/add
    - Instead you have to use:
        - /add?a=10&b=20
            - This will add 10 and 20 and the page will display the answer 30