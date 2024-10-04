from script_for_app.utils import openConnection, closeConnection, clear, bcolors

# QUERY: restituzione di tutti gli attori segnati "uncredited"

def menuItem9(ctrl):
    if ctrl == True:
        print(bcolors.OKGREEN + "9  - restituzione degli attori segnati come 'uncredited'" + bcolors.RESET)
    else:
        print("9  - restituzione degli attori segnati come 'uncredited'")

def query9():
    clear()
    menuItem9(True)

    db = openConnection()

    result = db.actors.find({'character': {"$regex": '[^.]?(uncredited)[^.]?'}}, {"_id": 0, "name": 1, "character": 1})

    if len(list(result.clone())) == 0:
        print(bcolors.FAIL + "Non sono presenti in DB attori segnalati come 'uncredited'" + bcolors.RESET)
    else:
        for doc in result:
            print('Nome: {0}, personaggio: {1}'.format(doc['name'], doc['character']))

    closeConnection()
    return
