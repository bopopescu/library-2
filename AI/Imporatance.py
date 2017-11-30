import math
from decimal import *
from operator import itemgetter, attrgetter
from util import *


def importanceList(Examples):
    queue = PriorityQueue()#store results

    for attributes in Examples:
        print ("Attribute: ", attributes['attributes'])
        numerator = 0
        denominator = 0
        #calculate entropy of each attribute.
        items = attributes['list']
        for i in items:
            numerator = numerator + i[0]
            denominator = denominator + i[1]

        q = float(numerator / (numerator + denominator))
        #print('Q: ', q)

        #calculate probability B(q)
        B = -(q * math.log(q, 2) + (1.0 - q) * math.log((1.0 - q), 2))
        #print('B: ', B)
        distinct = list()
        total = float()
        items = attributes['list']
        for i in items:
            if i[0] != 0 and i[1] != 0:
                Tk = float(((i[0] + i[1]) / 12))
                Bk = float((i[0] / (i[0] + i[1])))
                result = (Tk * ((Bk * math.log(Bk, 2)) + (1 - Bk) * math.log(1 - Bk, 2)))
                print('Result: ', round(result, 6))
                total = (total + round(result, 6))
                print('TOTAL: ', total)

        final = B + total
        #print(final)
        queue.push( attributes['attributes'], final)

    return queue


def importance(attribute):

    numerator = 0
    denominator = 0
    getcontext().prec = 2
    for d in attribute:
        numerator = Decimal(numerator + d[0])
        denominator = Decimal(denominator + d[1])
    q = float(numerator / ( numerator + denominator))
    #print('Q: ',q)

    B = -(q * math.log(q, 2) + (1.0 - q) * math.log((1.0 - q), 2))
    #print('B: ', Decimal(B))
    distinct = list()
    total = float()
    for d in attribute:
        if d[0] != 0 and d[1] != 0:
            Tk = float(((d[0] + d[1]) / 12))
            Bk = float((d[0] / (d[0] + d[1])))
            result = (Tk * ((Bk * math.log(Bk, 2)) + (1 - Bk) * math.log(1 - Bk, 2)))
            #print('Result: ', round(result,6))
            total = (total + round(result,6))
            #print('TOTAL: ', total)
    final  = B + total
    print (final)