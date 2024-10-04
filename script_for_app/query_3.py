from script_for_app.utils import openConnection, closeConnection, clear, bcolors

#QUERY : Restituzione di una serie tv prodotta in un determinato arco di tempo

def menuItem3(ctrl):
    if ctrl == True:
        print(bcolors.OKGREEN + "3  - restituzione serie tv prodotte in un arco di tempo d'interesse" + bcolors.RESET)
    else:
        print("3  - restituzione serie tv prodotte in un arco di tempo d'interesse")

def query3():
    clear()
    menuItem3(True)

    db = openConnection()

    try:
        annoS1 = int(input(bcolors.BOLD + ">>>>> Inserisci primo anno: " + bcolors.RESET))
        annoS2 = int(input(bcolors.BOLD + ">>>>> Inserisci secondo anno: " + bcolors.RESET))

        result = db.shows.find({'release_year': {"$gt": annoS1, "$lt": annoS2}}, {'_id': 0,'title':1})

        if len(list(result.clone())) == 0:
            print(bcolors.FAIL + "Non sono presenti in DB serie tv prodotte nell'arco di tempo indicato" + bcolors.RESET)
        else:
            for doc in result:
                print('title: {0}'.format(doc['title']))
    except ValueError:
        print(bcolors.FAIL + "L'intervallo di tempo deve essere indicato tramite soli valori numerici" + bcolors.RESET)

    closeConnection()
    return