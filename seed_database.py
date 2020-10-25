"""Script to seed database."""

import os

import json

from datetime import datetime

import crud

import model

import server


os.system('dropdb YourFolderUnderscoredAsDatabaseNameHere')

os.system('createdb YourFolderUnderscoredAsDatabaseNameHere')

model.connect_to_db(server.app)

model.db.create_all()


# Create YourModelNameLowerCasedHere table's initial data.

with open('data/YourModelNameLowerCasedSingularHere.json') as f:

    YourModelNameLowerCasedSingularHere_data = json.loads(f.read())

YourModelNameLowerCasedSingularHere_in_db = []

for YourModelNameLowerCasedSingularHere in YourModelNameLowerCasedSingularHere_data:
    columnNamesSeparatedbyCommasUntilLastOne= (
                                   YourModelNameLowerCasedSingularHere['YourFirstColumnNameHere'],
                                   YourModelNameLowerCasedSingularHere['YourNextColumnNameHereTillLast'],
                                   YourModelNameLowerCasedSingularHere['YourLastColumnNameHere'])

    db_YourModelNameLowerCasedSingularHere = crud.create_YourModelNameLowerCasedSingularHere(
                                 YourFirstColumnNameHere,
                                 YourNextColumnNameHereTillLast,
                                 YourLastColumnNameHere)

    YourModelNameLowerCasedSingularHere_in_db.append(db_YourModelNameLowerCasedSingularHere)
