from script_for_app.utils import openConnection, closeConnection, clear, bcolors

# QUERY: restituzione di un film di genere animation al di sopra della durata di 100 minuti
def menuItem8(ctrl):
    if ctrl == True:
        print(bcolors.OKGREEN + "8  - restituzione film di genere 'animation' di durata>=100 " + bcolors.RESET)
    else:
        print("8  - restituzione film di genere 'animation' di durata>=100")

def query8():
    clear()
    menuItem8(True)

    db = openConnection()

    result = db.movies.find({'genres': {"$regex": "[^.]?animation[^.]?"}, 'runtime': {"$gte": 100}}, {"_id": 0, "title": 1, "description": 1, "runtime": 1})

    if len(list(result.clone())) == 0:
        print(bcolors.FAIL + "Non sono presenti in DB film di animazione con durata inferiore a quella indicata" + bcolors.RESET)
    else:
        for doc in result:
            print('titolo: {0}, runtime: {2}\ndescrizione: {1} \n'.format(doc['title'], doc['description'], doc['runtime']))

    closeConnection()
    return