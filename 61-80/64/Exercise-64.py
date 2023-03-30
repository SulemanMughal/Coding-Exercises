def check(X):
    if sorted(set(X)) == lst:
        return 'increasing'
    if sorted(set(X),reverse=True) == X:
        return 'decreasing'
    return 'neither'