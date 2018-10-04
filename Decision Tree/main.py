import operator

def gini(labels, rows):
    gini_scores_list = dict()
    for label in labels:
        # get category
        # get row for category
        row = rows[label]
        # calculate TRUE Gini
        t = row[0]
        ty = t[0]
        tn = t[1]

        impurity_true = 1
        impurity_true -= ((ty / (ty + tn)) ** 2) + ((tn / (ty + tn)) ** 2)

        # calculate FALSE Gini
        false = row[1]
        fy = false[0]
        fn = false[1]

        impurity_false = 1
        impurity_false -= ((fy / (fy + fn)) ** 2) + ((fn / (fy + fn)) ** 2)

        # calculate weighted average
        # weighted ave = giniT(total T/ Total T + F) + giniF(total T/Total T + F)
        weighted_ave = impurity_true*((ty+tn)/(ty+tn+fy+fn))+(impurity_false*((fy+fn)/(ty+tn+fy+fn)))
        gini_scores_list.update({label: weighted_ave})
    return gini_scores_list



rows = {'chest_pain':[(105,39),(34,125)],
       'blood_circ':[(37,127),(100,33)],
       'artiers':[(92,31),(45,129)]}

labels = ['chest_pain', 'blood_circ', 'artiers']

gini_scores = gini(labels, rows)

sorted_by_value = sorted(gini_scores.items(), key=lambda kv: kv[1], reverse=False)

print(sorted_by_value)