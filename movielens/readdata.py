def load_movielens(path='./movielens/ml-100k'):
    # get movie titles
    movies = {}
    for line in open(path + '/u.item', encoding='latin-1'):
        id, title = line.split('|')[0:2]
        movies[id] = title
    # load data
    prefs = {}
    for line in open(path + '/u.data', encoding='latin-1'):
        user, movieid, rating, ts = line.split('\t')
        prefs.setdefault(user, {})
        prefs[user][movies[movieid]] = float(rating)
    return prefs

prefs = load_movielens()['7']
a=prefs.keys()
print(a)