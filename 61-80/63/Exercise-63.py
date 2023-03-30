def pos_neg_sort(x): 
    pos = sorted([i for i in x if i>0],reverse=True)
    return [pos.pop() if j>0 else j for j in x]