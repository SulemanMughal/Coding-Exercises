def score_calculator(e, m, h):
    return 5*e+10*m+20*h if e+m+h == abs(e)+abs(m)+abs(h) else 'invalid'