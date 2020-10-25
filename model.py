from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()

# test = YourClassNameHereInTitleCaseSingular(channel_name='WinningCheckers', email_date='2020-01-31',number_subscribers = '1', month_end_at='2019-12-31', subscribers='0', views='1', minutes_watched='2', likes='3', comments='4', posts='5', shares='6')

class YourClassNameHereInTitleCaseSingular(db.Model):
    """A class for creator ."""
    
    __tablename__ = 'YourTableNameHereLowerCasePlural'

    YourPrimaryIDColumnNameHereLowerCase_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    YourColumnNameHereLowerCase = db.Column(YourDBTypeHereAsdb.typeSuchAsStringIntegerDate)

# keep repeating till all column names finished

    def __repr__(self):
        return f'<YourClassNameHereInTitleCaseSingular YourPrimaryKeyVariableHere={self.YourPrimaryKeyVariableHere} SecondColumnVariableNameHere={self.SecondColumnVariableNameHere}>'

def connect_to_db(flask_app, db_uri='postgresql:///YourDatabaseNamehere', echo=True):
   
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
   
    flask_app.config['SQLALCHEMY_ECHO'] = echo
   
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':

    from server import app

    connect_to_db(app)