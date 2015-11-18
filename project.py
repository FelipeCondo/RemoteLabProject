from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, appInputs, appOutputs

app = Flask(__name__)

engine = create_engine('sqlite:///appdata.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def mainPage():
    app_inputs = session.query(appInputs)
    return render_template('main.html', app_inputs=app_inputs)

@app.route('/new', methods=['GET', 'POST'])
def newPIDInputs():
    if request.method == 'POST':
        PIDInputs = appInputs(kp=request.form['coefkp'], ki=request.form['coefki'],
            kd=request.form['coefkd'], description=request.form['description'],
            setpoint=request.form['setpoint'])
        session.add(PIDInputs)
        session.commit()
        return redirect(url_for('mainPage'))
    else:
        return render_template('new.html')
        
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=30577)
