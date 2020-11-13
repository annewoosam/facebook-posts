from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()

class Facebookpost(db.Model):
    """A class for Facebookpost."""
    
    __tablename__ = 'facebookposts'

    channel_name = db.Column(db.Integer, autoincrement=True, primary_key=True)

    published_by = db.Column(db.String)

    url = db.Column(db.String)

    people_reached = db.Column(db.String)

    engagement = db.Column(db.String)

    like = db.Column(db.String)

    comment = db.Column(db.String)

    notes = db.Column(db.String)

    last_updated = db.Column(db.String)

    def __repr__(self):
        return f'<Facebookpost facebookpost_id={self.facebookpost_id} channel_name={self.channel_name}>'

def connect_to_db(flask_app, db_uri='postgresql:///facebook_posts', echo=True):
   
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
   
    flask_app.config['SQLALCHEMY_ECHO'] = echo
   
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':

    from server import app

    connect_to_db(app)