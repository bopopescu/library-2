from SortDates import sortDate
from datetime import date
from Queue import *


def main():

    date1 = date(2018,01,12)
    date2 = date(2018,01,12)
    date3 = date(2018,01,13)
    date4 = date(2018,01,10)

    print ('Sorted Dated Starting')
    one = ('apple', date1)
    two = ('banana', date2)
    three = ('orange', date3)
    four = ('grape', date4)
    listOfObjects = [one, two, three, four]
    q = sortDate(listOfObjects, 1)
    while q.not_empty:
        c = q.get()
        print c

    """
    education: 1 = college, 2 = University, 3 = Masters
    travel: 0,1,2,3,4,5,6,7,8,9,10 = 0% to 100%
    industry:
    location:
    :return:
    """
    sortDate()
    sk1 = [('Java', 4), ('python', 2), ('php',4), ('JavaScript', 3),('MySQL', 4), ('React', 2)]
    sk2 = [('C#', 2), ('python', 2), ('php', 4), ('SQL', 4), ('Angular', 2)]
    sk3 = [('C', 4), ('C++', 2), ('JavaScript', 3), ('MySQL', 4), ('React', 2)]
    sk4 = [('Ruby', 7), ('Go', 5), ('JavaScript', 3), ('MySQL', 4), ('React', 2)]
    sk5 = [('Java', 14), ('C++', 5), ('C#', 3), ('MySQL', 4), ]
    sk6 = [('C', 6), ('C++', 5), ('Python', 3), ('Andriod', 3)]
    sk7 = [('Python', 7), ('Go', 5), ('Angular', 3), ('MySQL', 4), ('CSS', 4)]
    sk8 = [('Java', 2), ('C#', 1), ('React', 2), ('MySQL', 3), ('CSS', 1)]
    sk9 = [('Java', 4), ('Go', 2), ('JavaScript', 2), ('MySQL', 3), ('CSS', 5)]
    sk10 = [('Java', 1), ('C++', 2), ('MySQL', 3), ('CSS', 5)]

    ed1 = 1
    ed2 = 2
    ed3 = 2
    ed4 = 2
    ed5 = 3
    ed6 = 1
    ed7 = 3
    ed8 = 2
    ed9 = 2
    ed10 = 1

    t1 = 1
    t2 = 2
    t3 = 2
    t4 = 4
    t5 = 3
    t6 = 7
    t7 = 5
    t8 = 3
    t9 = 6
    t10 = 4

    contractor_list = [{'name':'Gary','skill':sk1,'travel':t1 ,'education':ed1}, {'name':'Bill','skill':sk2, 'travel':t2 ,'education':ed2},
                       {'name':'Joe','skill':sk3, 'travel':t3 ,'education':ed3}, {'name':'Bob','skill': sk4, 'travel': t4, 'education': ed4},
                       {'name':'Janet','skill':sk5, 'travel':t5 ,'education':ed5},{'name':'Karen','skill':sk6, 'travel':t6 ,'education':ed6},
                       {'name':'Chuch','skill': sk7, 'travel': t7, 'education': ed7},{'name':'Nick','skill':sk8, 'travel':t8 ,'education':ed8},
                       {'name':'Steve','skill':sk9, 'travel':t9 ,'education':ed9},{'name':'Shawn','skill': sk10, 'travel': t10, 'education': ed10}]

    eSkills = [('Java',2), ('MySQL', 2)]
    cTravel = 2
    eEd = 2
    criteria =   {'search':'Software Analyst', 'cSkills':eSkills,'cTravel':cTravel, 'cEd':eEd}

    travel_list= list()
    for contractor in contractor_list:
        trvl = contractor['travel']
        if trvl >= 2: #travel time criteria
            travel_list.append(contractor)

    # get contractors based on skills
    skill_list = list()
    skill_match = len(eSkills)   # number of criteria in skills list

    for contractor in travel_list:
        sk = contractor['skill']
        count = 0
        for e_s in eSkills:
            for c_s in sk:
                if e_s[0] == c_s[0] and e_s[0] <= c_s[0]:
                    count += 1

        if float(count) >= skill_match:
            skill_list.append(contractor)

    #get contractors based on education
    education_list = list()
    for contractor in skill_list:
        ed = contractor['education']
        print("Ed: ", ed)
        if eEd <= ed:
            education_list.append(contractor)

    for a in education_list:
        print(a)

if __name__ == "__main__": main()