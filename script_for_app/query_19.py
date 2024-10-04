from script_for_app.utils import openConnection, closeConnection, clear, bcolors

# QUERY: Inserimento di un nuovo regista e una nuova serie tv da lui diretto

def menuItem19(ctrl):
    if ctrl == True:
        print(bcolors.OKGREEN + "19 - inserimento di un nuovo regista ed una nuova serie tv da lui diretta" + bcolors.RESET)
    else:
        print("19 - inserimento di un nuovo regista ed una nuova serie tv da lui diretta")

def query19():
    clear()
    menuItem19(True)

    db = openConnection()

    try:
        print("Caricamento dati del regista...")
        director = input(bcolors.BOLD + ">>>>> Inserisci nome e cognome :" + bcolors.RESET)
        person_id = int(input(bcolors.BOLD + ">>>>> Inserisci id numerico di riconoscimento univoco:" + bcolors.RESET))
        idShow = input(bcolors.BOLD + ">>>>> Inserisci id della serie tv che ha diretto:" + bcolors.RESET)

        print("Caricamento dati della serie tv...")
        title = input(bcolors.BOLD + ">>>>> Inserisci titolo:" + bcolors.RESET)
        description = input(bcolors.BOLD + ">>>>> Inserisci descrizione:" + bcolors.RESET)
        release_year = int(input(bcolors.BOLD + ">>>>> Inserisci anno di uscita:" + bcolors.RESET))
        age_certification = input(bcolors.BOLD + ">>>>> Inserisci certificazione d'età:" + bcolors.RESET)
        runtime = int(input(bcolors.BOLD + ">>>>> Inserisci durata degli episodi della serie tv espressa in minuti:" + bcolors.RESET))
        genres = input(bcolors.BOLD + ">>>>> Inserisci generi della serie tv:" + bcolors.RESET)
        production_contries = input(bcolors.BOLD + ">>>>> Inserisci paese di produzione:" + bcolors.RESET)
        seasons = int(input(bcolors.BOLD + ">>>>> Inserisci numero di stagioni previste:" + bcolors.RESET))

        result1 = db.directors.insert_one({"name": director, 'id': idShow, 'person_id':person_id})
        result2 = db.shows.insert_one({"id": idShow, "title": title,
                                        "description": description,
                                        "release_year": release_year,
                                        "age_certification": age_certification,
                                        "runtime": runtime,
                                        "genres": genres,
                                        "production_countries": production_contries,
                                        "seasons":seasons})

        print("inserimento avvenuto con successo")
    except ValueError:
        print(bcolors.FAIL + "L'id identificativo,anno di uscita,durata degli episodi e numero di stagioni devono essere valori numerici" + bcolors.RESET)

    closeConnection()
    return
