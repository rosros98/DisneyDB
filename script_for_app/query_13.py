from script_for_app.utils import openConnection, closeConnection, clear, bcolors

# QUERY: restituzione di tutte le serie tv in cui ha partecipato un determinato attore

def menuItem13(ctrl):
    if ctrl == True:
        print(bcolors.OKGREEN + "13 - restituzione serie tv in cui ha partecipato un determinato attore" + bcolors.RESET)
    else:
        print("13 - restituzione serie tv in cui ha partecipato un determinato attore")

def query13():
    clear()
    menuItem13(True)

    db = openConnection()

    actor = input(bcolors.BOLD + ">>>>> Inserisci nome dell'attore:" + bcolors.RESET)

    result = db.actors.aggregate([
        {'$match': {'name': actor}}, #per estrarre dalla collection actors i documenti indicanti l'actor indicato
        {'$lookup':
             {'from': 'shows',
              'localField': 'id',
              'foreignField': 'id',
              'as': 'showsActor'}},
        {'$project':{'_id': 0, 'imdb_id': 0, 'imdb_score': 0, 'imdb_votes': 0, 'tmdb_popularity': 0, 'tmdb_score': 0}}
    ])

    if not result.alive:
        print(bcolors.FAIL + "Non sono presenti in DB serie tv in cui l'attore ha partecipato" + bcolors.RESET)
    else:
        for doc in result:
            list = doc['showsActor']
            for x in list:
                try:
                    print('title: {0} ({1})\ndescription: {2}\ngenere: {3} - certificazione età: {4} - paesi di produzione: {5}\n{6} stagioni con episodi di {7} min'.format(x['title'],x['release_year'], x['description'],x['genres'],x['age_certification'],x['production_countries'],x['seasons'],x['runtime']))
                except KeyError:
                    print('title: {0} ({1})\ndescription: {2}\ngenere: {3} - certificazione età: assente - paesi di produzione: {4}\n{5} stagioni con episodi di {6} min'.format(x['title'],x['release_year'], x['description'],x['genres'],x['production_countries'],x['seasons'],x['runtime']))

    closeConnection()
    return