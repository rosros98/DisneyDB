from script_for_app.utils import openConnection, closeConnection, clear, bcolors

# QUERY: Aggiornamento della certificazione d'età per tutti i film prodotti tra il 1900 e il 1950

def menuItem20(ctrl):
    if ctrl == True:
        print(bcolors.OKGREEN + "20 - update cerfiticazione d'età per tutti i film prodotti tra il 1900 e il 1950" + bcolors.RESET)
    else:
        print("20 - update cerfiticazione d'età per tutti i film prodotti tra il 1900 e il 1950")

def query20():
    clear()
    menuItem20(True)

    db = openConnection()

    age_cert = input(bcolors.BOLD + ">>>>> Inserisci la nuova certificazione d'età d'assegnare: " + bcolors.RESET)

    result = db.movies.find({'release_year': {"$gte": 1900, "$lte": 1950}}, {'_id':0, 'id':0,'imdb_id': 0,'imdb_votes': 0,'tmdb_popularity': 0,'tmdb_score': 0})
    print(bcolors.OKGREEN + "\nRecupero i film che rispettano le condizioni..." + bcolors.RESET)
    for doc in result:
        try:
            print('title: {0} (certificazione età: {1})'.format(doc['title'],doc['age_certification']))
        except KeyError:
            # vuol dire che il film combacia per anno di rilascio, ma non riporta age_certification -> inserimento diretto
            print('title: {0} (certificazione età: assente)'.format(doc['title']))

    db.movies.update_many({'release_year': {"$gte": 1900, "$lte": 1950}}, {"$set": {"age_certification": age_cert}})

    result = db.movies.find({'release_year': {"$gte": 1900, "$lte": 1950}}, {'_id':0, 'id':0,'imdb_id': 0,'imdb_votes': 0,'tmdb_popularity': 0,'tmdb_score': 0})
    print(bcolors.OKGREEN + "\nRecupero i film che rispettano le condizioni aggiornati..." + bcolors.RESET)
    for doc in result:
        print('title: {0} (certificazione età: {1})'.format(doc['title'], doc['age_certification']))

    closeConnection()
    return