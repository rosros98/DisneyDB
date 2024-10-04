from script_for_app.utils import openConnection, closeConnection, clear, bcolors

# QUERY: Restituzione degli show con specifico age certification in cui l’attore ha partecipato
def menuItem10(ctrl):
    if ctrl == True:
        print(bcolors.OKGREEN + "10 - restituzione serie tv in cui un dato attore ha partecipato e aventi specifico age_certification" + bcolors.RESET)
    else:
        print("10 - restituzione serie tv in cui un dato attore ha partecipato e aventi specifico age_certification")

def query10():
    clear()
    menuItem10(True)

    db = openConnection()

    age = input(bcolors.BOLD + ">>>>> Inserisci l'age certification:" + bcolors.RESET)
    actor = input(bcolors.BOLD + ">>>>> Inserisci nome attore:" + bcolors.RESET)

    result = db.actors.aggregate([{"$match": {"name": actor, 'id': {"$regex": '[^.]?ts[^.]?'}}},
                                  {"$lookup": {"from": "shows",
                                               'localField':'id',
                                               'foreignField':'id',
                                               "pipeline": [{"$match": {"$expr": {"$eq": ['$age_certification', age]}}}],
                                               "as": "shows"}}])

    if not result.alive:
        print(bcolors.FAIL + "Non sono presenti in DB serie tv che rispettano le condizioni date" + bcolors.RESET)
    else:
        for doc in result:
            list = doc['shows']
            for x in list:
                print('title: {0} ({1})\ndescription: {2}\ngenere: {3} - certificazione età: {4} - paesi di produzione: {5}\nstagioni: {6} per episodi di {7} minuti\n'.format(x['title'],x['release_year'],x['description'],x['genres'],x['age_certification'],x['production_countries'],x['seasons'],x['runtime']))

    closeConnection()
    return