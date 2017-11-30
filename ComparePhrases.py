


def comparePhrases(jobPhrases, resPhrases):

    seen = set()
    misslist = []
    hitlist = []
    for phrase in jobPhrases:
        t = phrase
        if t not in resPhrases:
            seen.add(t)
            misslist.append(phrase)
        else:
            hitlist.append(phrase)

    return [misslist, hitlist]