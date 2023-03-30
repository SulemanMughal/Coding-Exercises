def get_frequencies(fs):
    return {x:fs.count(x) for x in fs}


get_frequencies(["A", "B", "A", "A", "A"]) 