def grouping(words):
    words.sort(key=str.lower)
    groups = {}
    for w in words:
        cap = sum(map(str.isupper, w))
        if cap in groups:
            groups[cap].append(w)
        else:
            groups[cap] = [w]
    return groups