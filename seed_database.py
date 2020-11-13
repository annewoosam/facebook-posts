"""Script to seed database."""

import os

import json

from datetime import datetime

import crud

import model

import server


os.system('dropdb facebook_posts')

os.system('createdb facebook_posts')

model.connect_to_db(server.app)

model.db.create_all()


# Create facebookposts table's initial data.

with open('data/facebookpost.json') as f:

    facebookpost_data = json.loads(f.read())

facebookpost_in_db = []

for facebookpost in facebookpost_data:
    columnNamesSeparatedbyCommasUntilLastOne= (
                                   facebookpost['channel_name'],
                                   facebookpost['what'],
                                   facebookpost['published_by'],
                                   facebookpost['url'],
                                   facebookpost['people_reached'],
                                   facebookpost['engagement'],
                                   facebookpost['like'],
                                   facebookpost['comment'],
                                   facebookpost['notes'],
                                   facebookpost['last_updated'])

    db_facebookpost = crud.create_facebookpost(
                                 channel_name,
                                 what,
                                 published_by,
                                 url,
                                 people_reached,
                                 engagement,
                                 like,
                                 comment,
                                 notes,
                                 last_updated)

    facebookpost_in_db.append(db_facebookpost)
