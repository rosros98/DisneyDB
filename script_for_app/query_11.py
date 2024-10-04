from script_for_app.utils import openConnection, closeConnection, clear, bcolors

# QUERY: Eliminazione di un film e di tutte le occorrenze in directors e actors ad esso associati

def menuItem11(ctrl):
    if ctrl == True:
        print(bcolors.OKGREEN + "11 - eliminazione di un film" + bcolors.RESET)
    else:
        print("11 - eliminazione di un film")

def query11():
    clear()
    menuItem11(True)

    db = openConnection()

    title = input(bcolors.BOLD + ">>>>> Inserisci titolo del film:" + bcolors.RESET)

    result = db.movies.find({'title':title}) #recupero il film

    if len(list(result.clone())) == 0:
        print(bcolors.FAIL + "Non è stato possibile eliminare il film indicato perché non presente in DBsi" + bcolors.RESET)
    else:
        for doc in result:
            idFilm = doc['id']  # recupero l'id del film per fare le ricerche nelle altre collezioni

            db.directors.delete_many({'id':idFilm}) #cancello i direttori del film
            db.actors.delete_many({'id':idFilm}) #cancello gli attori che hanno partecipato a quel film

        db.movies.delete_many({'title':title})  # cancello il film

        print('Successful delete')

    closeConnection()
    return