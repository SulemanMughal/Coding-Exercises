def zipper(lst1, lst2):
    if lst1==lst2: return True
    elif lst1[-1]!=lst2[-1]: return False
    for i in range(2, len(lst1)+1):
        if lst1[-i]!= lst2[-i]:
            return [len(lst1)-i, len(lst2)-i]