"""CRUD operations."""

from model import db, YourClassNameHereInTitleCaseSingular, connect_to_db

import datetime


def create_YourClassNameHereInLowerCaseSingular(YourColumnNamesHereSeparatedByCommasExcludingPrimaryKeyColumn):
   

    YourClassNameHereInLowerCaseSingular = YourClassNameHereInTitleCaseSingular(YourColumnName=YourColumnName,
                  YourNextColumnNameUntilLast=YourNextColumnNameUntilLast,
                  YourLastColumnName=YourLastColumnName)

    db.session.add(YourClassNameHereInLowerCaseSingular)

    db.session.commit()

    return YourClassNameHereInLowerCaseSingular

def get_YourClassNameHereInLowerCasePlural():
    """Return all rows of YourClassNameHereInLowerCaseSingular monthly data."""

    return YourClassNameHereInTitleCaseSingular.query.all()
 
if __name__ == '__main__':
    from server import app
    connect_to_db(app)
