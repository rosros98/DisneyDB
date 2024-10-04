from script_for_app.utils import openConnection, closeConnection, clear, bcolors

# QUERY: Ricercare per un determinato attore, tutti i personaggi che ha interpretato e poi:
# se ha interpretato una voce, andiamo a cercare il film canadese in cui lo ha fatto e restituiamo la descrizione

def menuItem18(ctrl):
    if ctrl == True:
        print(bcolors.OKGREEN + "18 - restituzione per un determinato attore, di tutti i personaggi interpretati come voce in film canadesi" + bcolors.RESET)
    else:
        print("18 - restituzione per un determinato attore, di tutti i personaggi interpretati come voce in film canadesi")

def query18():
    clear()
    menuItem18(True)

    db = openConnection()

    actor = input(bcolors.BOLD + ">>>>> Inserisci nome dell'attore:" + bcolors.RESET)

    result = db.actors.aggregate([
        {'$match': {'name': actor, 'character': {"$regex": '[^.]?(voice)[^.]?'}}},
        {'$lookup': #cerchiamo i film in cui l'attore ha partecipato
             {'from': 'movies',
              'localField': 'id',
              'foreignField': 'id',
              'pipeline': [{
                  "$match": {
                      '$expr': {
                          "$and": [
                              {'$regexFind': {'input': "$production_countries", 'regex': '[^.]?CA[^.]?'}}
                          ]}}}],
              'as': 'filmsActor'}}
    ])

    if not result.alive:
        print(bcolors.FAIL + "Non sono presenti in DB film per cui sono rispettate le condizioni date" + bcolors.RESET)
    else:
        for doc in result:
            list = doc['filmsActor']
            for x in list:
                try:
                    print('title: {0} ({1} - {2} min)\ndescription: {3}\ngenere: {4} - certificazione età: {5} - paesi di produzione: {6}\n'.format(x['title'], x['release_year'], x['runtime'], x['description'], x['genres'],x['age_certification'], x['production_countries']))
                except KeyError:
                    print('title: {0} ({1} - {2} min)\ndescription: {3}\ngenere: {4} - certificazione età: assente - paesi di produzione: {5}\n'.format(x['title'], x['release_year'], x['runtime'], x['description'], x['genres'],x['production_countries']))

    closeConnection()
    return
