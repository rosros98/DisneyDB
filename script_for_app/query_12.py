from script_for_app.utils import openConnection, closeConnection, clear, bcolors

# QUERY: restituzione tutti i film diretti da un determinato regista

def menuItem12(ctrl):
    if ctrl == True:
        print(bcolors.OKGREEN + "12 - restituzione dei film diretti da un determinato regista" + bcolors.RESET)
    else:
        print("12 - restituzione dei film diretti da un determinato regista")

def query12():
    clear()
    menuItem12(True)

    db = openConnection()

    director = input(bcolors.BOLD + ">>>>> Inserisci nome del regista:" + bcolors.RESET)

    result = db.directors.aggregate([
        {'$match': {'name': director}}, #per estrarre dalla collection directors i documenti indicanti il direttore indicato
        {'$lookup':
             {'from': 'movies',
              'localField': 'id',
              'foreignField': 'id',
              'as': 'filmsDirector'}},
        {'$project':{'_id': 0, 'imdb_id': 0, 'imdb_score': 0, 'imdb_votes': 0, 'tmdb_popularity': 0, 'tmdb_score': 0}}
    ])

    if not result.alive:
        print(bcolors.FAIL + "Non sono presenti in DB film diretti dal regista indicato" + bcolors.RESET)
    else:
        for doc in result:
            list = doc['filmsDirector']
            for x in list:
                try:
                    print('title: {0} ({1} - {2} min)\ndescription: {3}\ngenere: {4} - certificazione età: {5} - paesi di produzione: {6}\n'.format(x['title'],x['release_year'],x['runtime'],x['description'],x['genres'],x['age_certification'],x['production_countries']))
                except KeyError:
                    print('title: {0} ({1} - {2} min)\ndescription: {3}\ngenere: {4} - certificazione età: assente - paesi di produzione: {5}\n'.format(x['title'],x['release_year'],x['runtime'],x['description'],x['genres'],x['production_countries']))

    closeConnection()
    return