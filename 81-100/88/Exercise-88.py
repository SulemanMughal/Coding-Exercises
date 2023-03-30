def double_letters(word):
    return any(letter*2 in word for letter in word)


double_letters('moon')
double_letters('fly')
double_letters('loop')
double_letters('programming')