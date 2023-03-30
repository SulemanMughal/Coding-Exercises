def calculate_score(games):
    count = 0
    for i in games:
        if i == ["R", "S"] or i == ["S", "P"] or i == ["P", "R"]:
            count += 1
        elif i[0] == i[1]:
            count += 0
        else:
            count -= 1
    if count > 0:
        return "John"
    elif count == 0:
        return "Tie"
    else:
        return "Sara"