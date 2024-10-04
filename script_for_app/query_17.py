from script_for_app.utils import openConnection, closeConnection, clear, bcolors

# QUERY: Restituzione delle serie tv o dei film in cui è presente un determinato attore
# dove, se si tratta di film, devono durare almeno 30 minuti altrimenti,
# se si tratta di serie tv, gli episodi devono durare almeno 30 minuti,
# sono stati rilasciati dal 2000 in poi negli US e sono di un particolare genere

def menuItem17(ctrl):
    if ctrl == True:
        print(bcolors.OKGREEN + "17 - restituzione serie tv o film in cui è presente un dato attore.\nSe si tratta di film, devono avere una durata>=30 minuti altrimenti se si tratta di serie, gli episodi devono avere una durata>=30, devono essere prodotti negli USA, usciti dal 2000 in poi e di un particolare genere" + bcolors.RESET)
    else:
        print("17 - restituzione serie tv o film in cui è presente un dato attore.\nSe si tratta di film, devono avere una durata>=30 minuti altrimenti se si tratta di serie, gli episodi devono avere una durata>=30, devono essere prodotti negli USA, usciti dal 2000 in poi e di un particolare genere")

def query17():
    clear()
    menuItem17(True)

    db = openConnection()

    actor = input(bcolors.BOLD + ">>>>> Inserisci nome dell'attore:" + bcolors.RESET)
    genres = input(bcolors.BOLD + ">>>>> Inserisci il genere del film o dello show:" + bcolors.RESET)

    regexCountries = "[^.]?US[^.]?"
    regexGenres = "[^.]?" + genres + "[^.]?"
    result = db.actors.aggregate([
        {'$match': {'name': actor}},
        {'$lookup': #cerchiamo film in cui l'attore ha partecipato
             {'from': 'movies',
              'localField': 'id',
              'foreignField': 'id',
              'pipeline': [{
                  '$match': {
                      '$expr': {
                          '$and': [
                              {'$gte': ['$release_year', 2000]},
                              {'$gte': ['$runtime', 30]},
                              {'$regexFind': {'input': "$production_countries", 'regex': regexCountries}},
                              {'$regexFind': {'input': "$genres", 'regex': regexGenres}}
                        ]}}}],
              'as': 'filmsActor'}},
        {'$lookup': #cerchiamo show in cui l'attore ha partecipato
             {'from': 'shows',
              'localField': 'id',
              'foreignField': 'id',
              'pipeline': [{
                  '$match': {
                      '$expr': {
                          '$and': [
                              {'$gte': ['$release_year', 2000]},
                              {'$gte': ['$runtime', 30]},
                              {'$regexFind': {'input': "$production_countries", 'regex': regexCountries}},
                              {'$regexFind': {'input': "$genres", 'regex': regexGenres}}
                        ]}}}],
              'as': 'showsActor'}}
    ])

    if not result.alive:
        print(bcolors.FAIL + "Non sono presenti in DB films e/o serie tv che rispettano le condizioni date per l'attore indicato" + bcolors.RESET)
    else:
        print("************* FILMS *************")
        for doc in result:
            list = doc['filmsActor']
            for x in list:
                try:
                    print('title: {0} ({1} - {2} min)\ndescription: {3}\ngenere: {4} - certificazione età: {5} - paesi di produzione: {6}\n'.format(x['title'], x['release_year'], x['runtime'], x['description'], x['genres'],x['age_certification'], x['production_countries']))
                except KeyError:
                    print('title: {0} ({1} - {2} min)\ndescription: {3}\ngenere: {4} - certificazione età: assente - paesi di produzione: {5}\n'.format(x['title'], x['release_year'], x['runtime'], x['description'], x['genres'],x['production_countries']))

        print("************* SHOWS *************")
        for doc in result:
            list = doc['showsActor']
            for x in list:
                try:
                    print('title: {0} ({1})\ndescription: {2}\ngenere: {3} - certificazione età: {4} - paesi di produzione: {5}\nstagioni: {6} di episodi da {7} min l\'uno'.format(x['title'], x['release_year'], x['description'], x['genres'],x['age_certification'], x['production_countries'], x['seasons'], x['runtime']))
                except KeyError:
                    print('title: {0} ({1})\ndescription: {2}\ngenere: {3} - certificazione età: assente - paesi di produzione: {4}\nstagioni: {5} di episodi da {6} min l\'uno'.format(x['title'], x['release_year'], x['description'], x['genres'],x['production_countries'], x['seasons'], x['runtime']))

    closeConnection()
    return
