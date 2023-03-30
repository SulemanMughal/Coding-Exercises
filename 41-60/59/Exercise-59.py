def split(txt):
    vowels = ''.join(ch for ch in txt if ch in 'aeiouAEIOU')
    others = ''.join(ch for ch in txt if ch not in 'aeiouAEIOU')
    return vowels+others