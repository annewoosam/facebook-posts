"""CRUD operations."""

from model import db, Facebookposts, connect_to_db

import datetime


def create_Facebookpost(what, published_by, url, people_reached, engagement, like, comment, notes, last_updated):
   

    Facebookpost = Facebookpost(what=what,
                  published_by=published_by,
                  url=url,
                  people_reached=people_reached,
                  engagement=engagement,
                  like=like,
                  comment=comment,
                  notes=notes,
                  last_updated=last_updated)

    db.session.add(Facebookpost)

    db.session.commit()

    return Facebookpost

def get_Facebookposts():
    """Return all rows of Facebookpost data."""

    return Facebookpost.query.all()
 
if __name__ == '__main__':
    from server import app
    connect_to_db(app)
