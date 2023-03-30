def swap_d(k, v, swapped):
    return dict(zip(v, k)) if swapped else dict(zip(k, v))