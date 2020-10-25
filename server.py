"""Server for YourFolder app."""

# increased flask

from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# created import allowing connection to database

from model import connect_to_db, YourModelNameTitleCaseSingularStats, db

app = Flask(__name__)

# imported Jinja secret key settings
from jinja2 import StrictUndefined

app.secret_key = "dev"

app.jinja_env.undefined = StrictUndefined

import crud

@app.route('/')

def all_YourModelNameLowerCasePluralStats():

    stats=crud.get_YourModelNameLowerCasePlural()
    
    YourVariableName=[q[0] for q in db.session.query(YourModelNameInTitleCaseHere.YourVariableName).all()]

    YourNextVariableName=[q[0] for q in db.session.query(YourModelNameInTitleCaseHere.YourNextVariableName).all()]
     
    #repeat till next to last variable accounted for
      
    YourLastVariableName=[q[0] for q in db.session.query(YourModelNameInTitleCaseHere.YourLastVariableName).all()]
    
    # repeat through all columns needed

    return render_template('YourModelNameLowerCasePlural.html', YourVariable_Name=YourVariable_Name, YourNextVariableName=YourNextVariableName, YourLastVariableName=YourLastVariableName)

if __name__ == '__main__':

# added connection to database

    connect_to_db(app)

# during development

    app.run(host='0.0.0.0', debug=True)

# in production

    #app.run()