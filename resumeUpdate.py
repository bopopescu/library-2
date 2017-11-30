import re
import nltk

def resumeUpdate(text):
    regexFirstLast = re.compile("[A-Z]\\w{2,20}\\s[A-Z]\\w{2,20}|[A-Z]\\w{2,20}\\s([A-Z]\\w{2,20}|[A-Z]\.)\\s[A-Z]\\w{2,20}")
    try:
        name = regexFirstLast.match(text)
        fname = name.group()
        return fname

    except Exception as e:
        return None

def getEmail(text):
    regexEmail = re.compile(r'[\w\.-]+@[\w\.-]+')
    try:
        em = regexEmail.search(text)
        email = em.group()
        return email

    except Exception as e:
        return None

