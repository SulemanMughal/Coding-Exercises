def final_direction(initial, turns):
    d = ['N', 'E', 'S', 'W']
    return d[(d.index(initial) + sum([1 if i == 'R' else -1 for i in turns]))%4]