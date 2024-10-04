from script_for_app.utils import clear, openConnection, closeConnection, bcolors

# QUERY : restituzione delle informazioni di un film con titolo inserito da utente

def menuItem1(ctrl):
    if ctrl == True:
        print(bcolors.OKGREEN + "1  - restituzione dettagli di un film d'interesse" + bcolors.RESET)
    else:
        print("1  - restituzione dettagli di un film d'interesse")


def query1():
    clear()
    menuItem1(True)

    db = openConnection()
    titolo = input(bcolors.BOLD + ">>>>> Inserisci il titolo del film da ricercare: " + bcolors.RESET)

    result = db.movies.find({'title': titolo},
                            {'_id': 0, 'id': 0, 'imdb_id': 0, 'imdb_score': 0, 'imdb_votes': 0, 'tmdb_popularity': 0,
                             'tmdb_score': 0})

    if len(list(result.clone())) == 0:
        print(bcolors.FAIL + "Il film ricercato non è presente in DB" + bcolors.RESET)
    else:
        for doc in result:
            print('title: {0} ({1} - {2} min)\ndescription: {3}\ngenere: {4} - certificazione età: {5} - paesi di produzione: {6}\n'.format(doc['title'], doc['release_year'], doc['runtime'], doc['description'], doc['genres'],doc['age_certification'], doc['production_countries']))

    closeConnection()
    return
