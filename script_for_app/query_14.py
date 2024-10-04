from script_for_app.utils import openConnection, closeConnection, clear, bcolors

# QUERY: restituzione tutti i film che un direttore ha diretto in un intervallo di tempo, di un dato genere con imdb_score maggiore di quello dato

def menuItem14(ctrl):
    if ctrl == True:
        print(bcolors.OKGREEN + "14 - restituzione film diretti da un dato regista in un intervallo di tempo dato, di dati genere e imdb_score" + bcolors.RESET)
    else:
        print("14 - restituzione film diretti da un dato regista in un intervallo di tempo dato, di dati genere e imdb_score")

def query14():
    clear()
    menuItem14(True)

    db = openConnection()

    try:
        director = input(bcolors.BOLD + ">>>>> Inserisci nome del regista:" + bcolors.RESET)
        inYear = int(input(bcolors.BOLD + ">>>>> Inserisci anno di partenza dell'intervallo:" + bcolors.RESET))
        endYear = int(input(bcolors.BOLD + ">>>>> Inserisci anno di termine dell'intervallo:" + bcolors.RESET))
        genres = input(bcolors.BOLD + ">>>>> Inserisci genere dei film:" + bcolors.RESET)
        score = float(input(bcolors.BOLD + ">>>>> Inserisci imdb_score minimo dei film:" + bcolors.RESET))

        regexGenres = "[^.]?" + genres + "[^.]?"
        result = db.directors.aggregate([
            {'$match': {'name': director}},
            {'$lookup':
                 {'from': 'movies',
                  'localField': 'id',
                  'foreignField': 'id',
                  'pipeline': [{
                      "$match": {
                          '$expr': {
                              "$and": [
                                  {'$gt': ['$release_year', inYear]},
                                  {"$lt": ['$release_year', endYear]},
                                  {'$gte': ['$imdb_score', score]},
                                  {'$regexFind': {'input': "$genres", 'regex': regexGenres}}
                              ]}}}],
                  'as': 'filmsDirector'
                  }},
            {'$project': {'_id': 0, 'imdb_id': 0, 'imdb_votes': 0, 'tmdb_popularity': 0, 'tmdb_score': 0}}
        ])

        if not result.alive:
            print(bcolors.FAIL + "Non sono presenti nel DB film diretti dal regista dato secondo quella condizione" + bcolors.RESET)
        else:
            for doc in result:
                list = doc['filmsDirector']
                for x in list:
                    try:
                        print('title: {0} ({1} - {2} min)\ndescription: {3}\ngenere: {4} - certificazione età: {5} - paesi di produzione: {6}\nimdb_score: {7}\n'.format(x['title'], x['release_year'], x['runtime'], x['description'], x['genres'], x['age_certification'], x['production_countries'], x['imdb_score']))
                    except KeyError:
                        print('title: {0} ({1} - {2} min)\ndescription: {3}\ngenere: {4} - certificazione età: assente - paesi di produzione: {5}\nimdb_score: {6}\n'.format(x['title'], x['release_year'], x['runtime'], x['description'], x['genres'],x['production_countries'], x['imdb_score']))
    except ValueError:
        print(bcolors.FAIL + "L'intervallo di tempo e lo score devono essere valori numerici" + bcolors.RESET)

    closeConnection()
    return


