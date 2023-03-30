def remove_indices(mylist, idxs):
    result = []
    for i, l in enumerate(mylist):
        if i not in idxs:
            result.append(l)
    return result


def test_remove_indices():
    assert remove_indices(["John", "Bob", "Charles", "Trev"], [0]) == ["Bob", "Charles", "Trev"]
    assert remove_indices(["John", "Bob", "Charles", "Trev"], [1, 2]) == ["John", "Trev"]