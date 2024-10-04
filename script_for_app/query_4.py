from script_for_app.utils import openConnection, closeConnection, clear, bcolors

#QUERY: inserimento di un attore e un suo relativo film

def menuItem4(ctrl):
    if ctrl == True:
        print(bcolors.OKGREEN + "4  - inserimento di un attore e del relativo film di partecipazione" + bcolors.RESET)
    else:
        print("4  - inserimento di un attore e del relativo film di partecipazione")

def query4():
    clear()
    menuItem4(True)

    db = openConnection()

    print("Sarà inserito l'attore Chris Pratt che ha interpretato \'Owen Grady\' nel film \'Jurassic World\'")
    result1 = db.actors.insert_one({"person_id": 26478,
                                    "id": "tm00001",
                                    "name": "Chris Pratt",
                                    "character": "Owen Grady"})

    result2 = db.movies.insert_one({"id": "tm00001",
                                    "title": "Jurassic World",
                                    "description": "Set 22 years after the events of Jurassic Park, Jurassic World takes place on the same fictional island of Isla Nublar, located off the Pacific coast of Costa Rica. A successful theme park of cloned dinosaurs, dubbed Jurassic World, has operated on the island for years, bringing John Hammond's dream to fruition.",
                                    "release_year": 2015,
                                    "age_certification": "G",
                                    "runtime": 124,
                                    "genres": "['adventure', 'action', 'fantasy']",
                                    "production_countries": "['US']",
                                    "imdb_id": "tt0000224",
                                    "imdb_score": 8.5,
                                    "imdb_votes": "ciao",
                                    "tmdb_popularity": 89.99,
                                    "tmdb_score": 8.0})

    print("inserimento avvenuto con successo")

    print(bcolors.OKGREEN + "\nrecupero dei dati inseriti nel DB..." + bcolors.RESET)
    result1 = db.actors.find_one({'name': 'Chris Pratt'})
    result2 = db.movies.find_one({'title': 'Jurassic World'})

    print('name: {0} - character: {1} ({2})'.format(result1['name'],result1['character'],result1['id']))
    print('\ntitle: {0} ({1} - {2} min)\ndescription: {3}\ngenere: {4} - certificazione età: {5} - paesi di produzione: {6}\n'.format(result2['title'], result2['release_year'], result2['runtime'], result2['description'], result2['genres'], result2['age_certification'],result2['production_countries']))

    closeConnection()
    return