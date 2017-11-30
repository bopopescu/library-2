

def compareResToJob(jobNouns, resNouns):
    missList = []
    hitList = []
    jobList = []
    resList = []

    print ("COMPARE RES TO JOB")
    for job in jobNouns:
        #print (job)
        jobList.append(job['original'])

    for res in resNouns:
        #print (res)
        resList.append(res['original'])

    for job in jobNouns:
        x = job['tagged']
        flag = any(res['tagged'] == x for res in resNouns)
        if not flag:
            #print ("Word does not exist: ", job['original'], " Count: ",job['count'])
            missList.append({'word': job['original'], 'count': job['count'], 'tagged': job['tagged']})
        else:
            hitList.append({'word': job['original'], 'count': job['count'], 'tagged': job['tagged']})


    return [missList, hitList]


def compareNoStem(jobNouns, resNouns):
    missList = []
    hitList = []
    jobList = []
    resList = []

    for job in jobNouns:
        jobList.append(job['word'])

    for res in resNouns:
        resList.append(res['word'])

    for job in jobNouns:
        x = job['word']
        flag = any(res['word'] == x for res in resNouns)
        if not flag:
            missList.append({'word': job['word'], 'count': job['count']})
        else:
            hitList.append({'word': job['word'], 'count': job['count']})

    return [missList, hitList]


