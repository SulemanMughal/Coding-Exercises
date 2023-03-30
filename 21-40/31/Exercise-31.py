def count_all(txt):
    return {
        'LETTERS': sum(1 for x in txt if x.isalpha()),
        'DIGITS': sum(1 for x in txt if x.isnumeric()),
    }

count_all("Python is the number 1 modern language from 4 programming languages")