from script_for_app.utils import openConnection, closeConnection, clear, bcolors

#QUERY: restituzione di tutte le serie tv aventi un numero specifico di stagioni

def menuItem6(ctrl):
    if ctrl == True:
        print(bcolors.OKGREEN + "6  - restituzione serie tv aventi un numero specifico di stagioni" + bcolors.RESET)
    else:
        print("6  - restituzione serie tv aventi un numero specifico di stagioni")

def query6():
    clear()
    menuItem6(True)

    db = openConnection()

    try:
        nSerie = int(input(bcolors.BOLD + ">>>>> Inserisci il numero di stagioni che le serie da ricercare devono avere: " + bcolors.RESET))

        result = db.shows.find({'seasons': nSerie},
                               {'_id': 0, 'imdb_id': 0, 'imdb_score': 0, 'imdb_votes': 0, 'tmdb_popularity': 0,
                                'tmdb_score': 0})

        if len(list(result.clone())) == 0:
            print(bcolors.FAIL + "Non sono presenti in DB serie tv con il numero di stagioni indicato" + bcolors.RESET)
        else:
            for doc in result:
                print('title: {0} ({1})\nstagioni: {2} per episodi di {3} minuti\n'.format(doc['title'],doc['release_year'],doc['seasons'],doc['runtime']))
    except ValueError:
        print(bcolors.FAIL + "Il parametro inserito non è del tipo atteso" + bcolors.RESET)

    closeConnection()
    return