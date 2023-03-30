def choose_only_integers(x):
    return [i for i in x if type(i)==int]


choose_only_integers([1, 'so', 2, 'too', 3, 'but', 4, 'soon', 5, 'every', 6, 'non', 7, 'right'])