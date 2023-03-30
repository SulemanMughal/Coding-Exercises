def same_vowel_group(w):
    first = set(w[0]) & set('aeiou')
    return [i for i in w if set(i) & set('aeiou') == first]