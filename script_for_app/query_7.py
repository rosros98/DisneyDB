from script_for_app.utils import openConnection, closeConnection, clear, bcolors

#QUERY:	restituzuione del film che ha tmdb_score>=8 e tmbd_popolarity>=100
def menuItem7(ctrl):
    if ctrl == True:
        print(bcolors.OKGREEN + "7  - restituzione film con tmdb_score>=8 e tmdb_popolarity>=100" + bcolors.RESET)
    else:
        print("7  - restituzione film con tmdb_score>=8 e tmdb_popolarity>=100")

def query7():
    clear()
    menuItem7(True)

    db = openConnection()

    result = db.movies.find({'tmdb_popularity': {"$gte": 100.0}, 'tmdb_score': {"$gte": 8.0}}, {"_id": 0, "title": 1, "tmdb_popularity": 1, "tmdb_score": 1})

    if len(list(result.clone())) == 0:
        print(bcolors.FAIL + "Non sono presenti in DB film con score e popularity indicate" + bcolors.RESET)
    else:
        for doc in result:
            print('titolo: {0}, popularity: {1}, score: {2}\n'.format(doc['title'], doc['tmdb_popularity'], doc['tmdb_score']))

    closeConnection()
    return