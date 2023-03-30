def map_letters(word):
    return {l: [i for i, x in enumerate(word) if x==l] for l in set(word)}