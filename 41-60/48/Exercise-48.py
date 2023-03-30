def is_set(cards):
    properties = ['color','number','shade','shape']
    set_properties = [len(set(c[p] for c in cards)) for p in properties]
    return all(prop == 1 or prop == 3 for prop in set_properties)