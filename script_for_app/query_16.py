from script_for_app.utils import openConnection, closeConnection, clear, bcolors

# QUERY: restituzione per un regista tutti i film e le serie tv che ha diretto e i relativi attori

def menuItem16(ctrl):
    if ctrl == True:
        print(bcolors.OKGREEN + "16 - restituzione per un dato regista dei film e delle serie che ha diretto e i relativi attori" + bcolors.RESET)
    else:
        print("16 - restituzione per un dato regista dei film e delle serie che ha diretto e i relativi attori")

def query16():
    clear()
    menuItem16(True)

    db = openConnection()

    director = input(bcolors.BOLD + ">>>>> Inserisci nome del regista:" + bcolors.RESET)

    result = db.directors.aggregate([
        {'$match': {'name': director}},
        {'$lookup': #cerchiamo film che il direttore ha diretto
             {'from': 'movies',
              'localField': 'id',
              'foreignField': 'id',
              'pipeline': [{ #cerchiamo la lista di attori che hanno partecipato ad ogni film trovato
                  '$lookup': {
                      'from': 'actors',
                      'localField': 'id',
                      'foreignField': 'id',
                      'as': 'actorsDirector'
                  }}],
              'as': 'filmsDirector'}},
        {'$lookup': #cerchiamo show che il direttore ha diretto
             {'from': 'shows',
              'localField': 'id',
              'foreignField': 'id',
              'pipeline': [{ #cerchiamo la lista di attori che hanno partecipato ad ogni show trovato
                  '$lookup': {
                      'from': 'actors',
                      'localField': 'id',
                      'foreignField': 'id',
                      'as': 'actorsDirector'
                  }}],
              'as': 'showsDirector'}}
    ])

    if not result.alive:
        print(bcolors.FAIL + "Non sono presenti nel DB film e/o serie diretti dal regista dato" + bcolors.RESET)
    else:
        print("************* FILMS *************")
        for doc in result:
            #recuperiamo i dettagli del film diretto
            list = doc['filmsDirector']
            for doc in list:
                print('title: {0} ({1})'.format(doc['title'], doc['release_year']))

                #recuperiamo la lista degli attori che hanno partecipato al film
                list = doc['actorsDirector']
                for doc in list:
                    try:
                        print('\tname: {0} - character: {1}'.format(doc['name'], doc['character']))
                    except KeyError:
                        print('\tname: {0} - character: absent'.format(doc['name']))

        print("\n************* SHOWS *************")
        for doc in result:
            # recuperiamo i dettagli del film diretto
            list = doc['showsDirector']
            for doc in list:
                print('title: {0} ({1})'.format(doc['title'], doc['release_year']))

                # recuperiamo la lista degli attori che hanno partecipato al film
                list = doc['actorsDirector']
                for doc in list:
                    try:
                        print('\tname: {0} - character: {1}'.format(doc['name'], doc['character']))
                    except KeyError:
                        print('\tname: {0} - character: absent'.format(doc['name']))

    closeConnection()
    return
