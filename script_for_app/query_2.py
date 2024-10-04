from script_for_app.utils import openConnection, closeConnection, clear, bcolors

#QUERY: restituzione del numero di stagioni relativo ad una data serie tv

def menuItem2(ctrl):
    if ctrl == True:
        print(bcolors.OKGREEN + "2  - restituzione numero di stagioni di una serie tv d'interesse" + bcolors.RESET)
    else:
        print("2  - restituzione numero di stagioni di una serie tv d'interesse")

def query2():
    clear()
    menuItem2(True)

    db = openConnection()

    titoloS = input(bcolors.BOLD + ">>>>> Inserisci il titolo serie:" + bcolors.RESET)

    result = db.shows.find({'title': titoloS}, {'_id': 0, 'seasons': 1})

    if len(list(result.clone())) == 0:
        print(bcolors.FAIL + "La serie tv ricercata non è presente in DB" + bcolors.RESET)
    else:
        for doc in result:
            print('stagioni: {0}\n'.format(doc['seasons']))

    closeConnection()
    return
