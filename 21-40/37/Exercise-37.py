GUEST_LIST = {
"Randy": "Germany",
"Emmma": "Germany",
    "Adalene": "France",
    "shushin": "Japan",
    "Robert": "England",
    "Tamer": "Egypt"
}


def greeting(name):
    if name in GUEST_LIST:
        return "Hi! I'm " + name+ ", and I'm from " + GUEST_LIST[name] + "."
    else:
        return "Hi! I'm a guest."