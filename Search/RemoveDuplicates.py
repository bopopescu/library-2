

def removeDups(list):
    seen = set()
    new_list = []
    for d in list:
        t = d
        if t not in seen:
            seen.add(t)
            new_list.append(d)

    return new_list