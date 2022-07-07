

from flask import Flask, render_template, redirect, request

import db_create as db 


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/returnToIndex')
def returnToIndex():
    return render_template('index.html')

@app.route('/pinSet')
def pinSet():
    return render_template('pin.html')

@app.route('/musicalSet')
def musicalSet():
    return render_template('musical.html')

@app.route('/graphicalSet')
def graphicalSet():
    return render_template('graphical.html')

@app.route('/informedConsentPage')
def informedConsentPage():
    return render_template('informedConsent.html')


@app.route('/surveyPage')
def surveyPage():
    return render_template('survey.html')


@app.route('/consentPageForm', methods=['POST'])
def consentPageForm():
    choice1 = request.form['choice1']
    choice2 = request.form['choice2']
    choice3 = request.form['choice3']
    choice4 = request.form['choice4']
    choice5 = request.form['choice5']
    choice6 = request.form['choice6']

    if request.method == 'POST':
            db.insert_details(choice1,choice2,choice3,choice4,choice5,choice6)

    return render_template('questions.html')


@app.route('/questionForm', methods=['POST'])
def questionForm():
    ansQ1 = request.form['q1']
    ansQ2 = request.form['q2']
    ansQ3 = request.form['q3']
    ansQ4 = request.form['q4']
    ansQ5a = request.form['q5a']
    ansQ5b = request.form['q5b']
    ansQ5c = request.form['q5c']
    ansQ5d = request.form['q5d']
    ansQComm5a = request.form['pinComment5a']
    ansQComm5b = request.form['pinComment5b']
    ansQComm5c = request.form['pinComment5c']
    ansQComm5d = request.form['pinComment5d']
    ansQ6 = request.form['q6']    
    ansQ7 = request.form['q7']
    ansQ6Comm = request.form['pinComment6']
    ansQ7Comm = request.form['pinComment7']


    #insert all the data to db
    if request.method == 'POST':
            db.insert_questdetails(ansQ1,ansQ2,ansQ3,ansQ4,ansQ5a,ansQ5b,ansQ5c,ansQ5d,ansQComm5a,ansQComm5b,ansQComm5c,ansQComm5d,ansQ6,ansQ7,ansQ6Comm,ansQ7Comm)
    return render_template('passwords.html')

@app.route('/passwordForm1', methods=['POST'])
def passwordForm1():
    username = request.form['username']
    password = request.form['password']
    print("username : " + username +"\n Password "+ password)
    #insert this data to db   
    if request.method == 'POST':
            db.insert_passdetails(username, password) 
    return render_template('passwordsLogin.html')

@app.route('/passwordLoginForm1', methods=['GET','POST'])
def passwordLoginForm1():
    username = request.form['username']
    password = request.form['password']
    attempt =1
    # print("username : " + username +"\n Password "+ password)
    exists = db.get_passdetails(username,password)
    print(exists)
    if exists == 'true':
            db.insert_passsuccess('yes','na','na')
            return render_template('pin.html') 
    else:
            return render_template('passwordsLogin2.html')

@app.route('/passwordLoginForm2', methods=['POST'])
def passwordLoginForm2():
    username = request.form['username']
    password = request.form['password']
    attempt =2
    print("username : " + username +"\n Password "+ password)
    exists = db.get_passdetails(username,password)
    print(exists)
    if exists == 'true':
            db.insert_passsuccess('no','yes','na')
            return render_template('pin.html') 
    else:
            return render_template('passwordsLogin3.html')
    #insert this data to db   
    #cross verify if data is correct with db. if so go to return render_template('pin.html') else go to below
    return render_template('passwordsLogin3.html')

@app.route('/passwordLoginForm3', methods=['POST'])
def passwordLoginForm3():
    username = request.form['username']
    password = request.form['password']
    attempt =3
    print("username : " + username +"\n Password "+ password)
    exists = db.get_passdetails(username,password)
    print(exists)
    if exists == 'true':
            db.insert_passsuccess('no','no','yes')
            return render_template('pin.html') 
    else:
            db.insert_passsuccess('no','no','no')
            return render_template('pin.html')
    #insert this data to db   
    return render_template('pin.html') 

@app.route('/pinForm1', methods=['POST'])
def pinForm1():
    username = request.form['username']
    pin = request.form['pin']
    print("username : " + username +"\n Password "+ pin)
    #insert this data to db   
    if request.method == 'POST':
        db.insert_pindetails(username, pin) 
    return render_template('pinLogin.html')

@app.route('/pinLoginForm1', methods=['POST'])
def pinLoginForm1():
    username = request.form['username']
    pin = request.form['pin']
    attempt =1
    print("username : " + username +"\n Password "+ pin)
    exists = db.get_pindetails(username,pin)
    print(exists)
    if exists == 'true':
            db.insert_pinsuccess('yes','na','na')
            return render_template('graphical.html') 
    else:
            return render_template('pinLogin2.html')
    #insert this data to db   
    #cross verify if data is correct with db. if so go to return render_template('graphical.html') else go to below

@app.route('/pinLoginForm2', methods=['POST'])
def pinLoginForm2():
    username = request.form['username']
    pin = request.form['pin']
    attempt =2
    print("username : " + username +"\n Password "+ pin)

    exists = db.get_pindetails(username,pin)
    print(exists)
    if exists == 'true':
            db.insert_pinsuccess('no','yes','na')
            return render_template('graphical.html') 
    else:
            return render_template('pinLogin3.html')
    #insert this data to db   
    #cross verify if data is correct with db. if so go to return render_template('graphical.html') else go to below

@app.route('/pinLoginForm3', methods=['POST'])
def pinLoginForm3():
    username = request.form['username']
    pin = request.form['pin']
    attempt =3
    print("username : " + username +"\n Password "+ pin)
    exists = db.get_pindetails(username,pin)
    print(exists)
    if exists == 'true':
            db.insert_pinsuccess('no','no','yes')
            return render_template('graphical.html') 
    else:
            db.insert_pinsuccess('no','no','no')
            return render_template('graphical.html')

    #insert this data to db   
    return render_template('graphical.html') 

@app.route('/graphicalForm1', methods=['POST'])
def graphicalForm1():
    username = request.form['username']
    listOfImg = request.form.getlist('imgs');
    listOfImg.sort()
    finstring=' '.join(listOfImg)
    print(finstring)
    #push these names to db
    if request.method == 'POST':
        db.insert_graphicaldetails(username, finstring) 
    return render_template('graphicalLogin.html')

@app.route('/graphicalLoginForm1', methods=['POST'])
def graphicalLoginForm1():
    listOfImg = request.form.getlist('imgs')
    attempt = 1
    username = request.form['username']
    listOfImg.sort()
    finstring=' '.join(listOfImg)
    exists = db.get_graphicaldetails(username,finstring)
    print(exists)
    if exists == 'true':
            db.insert_graphicalsuccess('yes','na','na')
            return render_template('musical.html') 
    else:
            return render_template('graphicalLogin2.html')
    #push these names to db 
    #retrieve previously inserted data and cross check; ensure to use "in op" so we wont have to worry about order
    #if match then go to return render_template('musical.html') else the one below
    return render_template('graphicalLogin2.html')

@app.route('/graphicalLoginForm2', methods=['POST'])
def graphicalLoginForm2():
    listOfImg = request.form.getlist('imgs');
    username = request.form['username']
    attempt = 2
    listOfImg.sort()
    finstring=' '.join(listOfImg)
    exists = db.get_graphicaldetails(username,finstring)
    print(exists)
    if exists == 'true':
            db.insert_graphicalsuccess('no','yes','na')
            return render_template('musical.html') 
    else:
            return render_template('graphicalLogin3.html')

    #push these names to db 
    #retrieve previously inserted data and cross check; ensure to use "in op" so we wont have to worry about order
    #if match then go to return render_template('musical.html') else the one below
    return render_template('graphicalLogin3.html')

@app.route('/graphicalLoginForm3', methods=['POST'])
def graphicalLoginForm3():
    listOfImg = request.form.getlist('imgs');
    username = request.form['username']
    attempt = 3
    #push these names to db 
    listOfImg.sort()
    finstring=' '.join(listOfImg)
    exists = db.get_graphicaldetails(username,finstring)
    print(exists)
    if exists == 'true':
            db.insert_graphicalsuccess('no','no','yes')
            return render_template('musical.html') 
    else:
            db.insert_graphicalsuccess('no','no','no')
            return render_template('musical.html')

    return render_template('musical.html')

@app.route('/musicalForm1', methods=['POST'])
def musicalForm1():
    musicName = request.form['music']
    username = request.form['username']
    #insert this value to db 
    if request.method == 'POST':
        db.insert_musicaldetails(username, musicName)    
    return render_template('musicalLogin.html')

@app.route('/musicalLoginForm1', methods=['POST'])
def musicalLoginForm1():
    musicName = request.form['music']
    username = request.form['username']
    attempt=1
    #push these names to db 
    #retrieve previously inserted data and cross check; 
    #if match then go to return render_template('survey.html') else the one below
    exists = db.get_musicaldetails(username,musicName)
    if exists == 'true':
            db.insert_musicalsuccess('yes','na','na')
            return render_template('survey.html') 
    else:
            return render_template('musicalLogin2.html')
    

    

@app.route('/musicalLoginForm2', methods=['POST'])
def musicalLoginForm2():
    musicName = request.form['music']
    username = request.form['username']
    attempt =2
    #push these names to db 
    #retrieve previously inserted data and cross check; 
    #if match then go to return render_template('survey.html') else the one below
    exists = db.get_musicaldetails(username,musicName)
    print(exists)
    if exists == 'true':
            db.insert_musicalsuccess('no','yes','na')
            return render_template('survey.html') 
    else:
            return render_template('musicalLogin3.html')


@app.route('/musicalLoginForm3', methods=['POST'])
def musicalLoginForm3():
    musicName = request.form['music']
    username = request.form['username']
    attempt =3
    #push these names to db 
    exists = db.get_musicaldetails(username,musicName)
    print(exists)
    if exists == 'true':
            db.insert_pinsuccess('no','no','no')
            return render_template('survey.html') 
    else:
            return render_template('survey.html')
    return render_template('survey.html')

@app.route('/surveyQuestion', methods=['POST'])
def surveyQuestion():
    ansQ1 = request.form['q1']
    ansQ2 = request.form['q2']
    ansQ3 = request.form['q3']
    ansQ4 = request.form['q4']
    ansQ1Comm = request.form['pinComment1']
    ansQ2Comm = request.form['pinComment2']
    ansQ3Comm = request.form['pinComment3']
    ansQ4Comm = request.form['pinComment4']
    ansQ5Comm = request.form['pinComment5']
    if request.method == 'POST':
        db.insert_surdetails(ansQ1,ansQ2,ansQ3,ansQ4,ansQ1Comm,ansQ2Comm,ansQ3Comm,ansQ4Comm,ansQ5Comm)
    return render_template('thankyou.html')


if __name__ == "__main__":
  app.run(debug=True)
