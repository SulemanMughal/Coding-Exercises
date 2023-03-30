def competition_rank(results, person):
    scores = list(results.values())
    for r in results:
        results[r] = (results[r],sum(1 for i in scores if i > results[r])+1)
    return results[person][1]