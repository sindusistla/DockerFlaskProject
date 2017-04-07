
# App.py

# import Flask
from flask import Flask,render_template,request, json
from pymongo import MongoClient

# create a app
app=Flask(__name__)
#mongodb://host/my_database
client=MongoClient('mongodb://db:27017/UsersDb');
#client=MongoClient('mongodb://localhost:27017/UsersDb')
db=client.UsersDb

# Basic route
@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST'])
def signUp():
    # read the posted values from the UI

    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    db.UsersDb.insert_one({"name":_name,"email":_email,"password":_password})

    # Retrieve the inserted record
    _items=db.UsersDb.find()
    items=[item for item in _items]
    print("item:",items);
    # validate the received values
    if _name and _email and _password:
        return render_template('HomePage.html',items=items)
        #return json.dumps({'html': '<span>All fields good !!</span>'})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)
    #app.run()

