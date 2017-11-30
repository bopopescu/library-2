import math
from AI.Imporatance import *

def main():

    #IMPORTANCE ALGORITHM
    patrons = {'attributes': 'patrons', 'list':([2,4],[4,0],[0,2])}
    alt = {'attributes': 'alt','list':([3,3], [3,3])}
    bar = {'attributes':'bar','list':([3,3], [3,3])}
    fri = {'attributes':'fri', 'list':([2,3],[4,3])}
    hun = {'attributes':'hun', 'list': ([5,2], [1,4])}
    price = {'attributes':'price', 'list':([4,3], [2,0], [1,2])}
    rain = {'attributes':'rain', 'list':([3,2], [3,4])}
    res = {'attributes':'res', 'list':([3,2], [3,4])}
    type = {'attributes':'type', 'list':([1,1], [2,2], [2,2], [1,1])}
    est = {'attributes': 'est', 'list':([4,2], [1,1], [1,1], [0,2])}

    examples = (patrons, alt, bar, fri, hun, price, rain, res, type, est)

    results = importanceList(examples)
    print('\n')
    print('RESULTS')
    while not results.isEmpty():
        item = results.pop()
        print (item)



if __name__ == "__main__": main()