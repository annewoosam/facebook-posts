"""Server for facebook-posts app."""

# increased flask

from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# created import allowing connection to database

from model import connect_to_db, Facebookpost, db

app = Flask(__name__)

# imported Jinja secret key settings
from jinja2 import StrictUndefined

app.secret_key = "dev"

app.jinja_env.undefined = StrictUndefined

import crud

@app.route('/')

def all_facebookposts():

    stats=crud.get_facebookposts()
    
    facebookpost_id=[q[0] for q in db.session.query(Facebookpost.facebookpost_id).all()]

    channel_name=[q[0] for q in db.session.query(Facebookpost.channel_name).all()]
     
    what=[q[0] for q in db.session.query(Facebookpost.what).all()]

    publised_by=[q[0] for q in db.session.query(Facebookpost.published_by).all()]

    url=[q[0] for q in db.session.query(Facebookpost.url).all()]

    people_reached=[q[0] for q in db.session.query(Facebookpost.people_reached).all()]

    engagement=[q[0] for q in db.session.query(Facebookpost.engagement).all()]

    like=[q[0] for q in db.session.query(Facebookpost.like).all()]

    comment=[q[0] for q in db.session.query(Facebookpost.comment).all()]

    notes=[q[0] for q in db.session.query(Facebookpost.notes).all()]
      
    last_updated=[q[0] for q in db.session.query(Facebookpost.last_updated).all()]

    return render_template('facebookposts.html', facebookpost_id=facebookpost_id, channel_name=channel_name, what=what, published_by, url, people_reached, engagement, like, comment, notes, last_updated)

if __name__ == '__main__':

# added connection to database

    connect_to_db(app)

# during development

    app.run(host='0.0.0.0', debug=True)

# in production

    #app.run()