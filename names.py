from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize import word_tokenize
import re
import nltk

class names(object):

    def __init__(self,text):

        self.text = text

    def out(self):
        stanford_dir = '/home/gary/stanford-ner-2015-04-20/'
        jarfile = stanford_dir + 'stanford-ner.jar'
        modelfile = stanford_dir + 'classifiers/english.all.3class.distsim.crf.ser.gz'
        st = StanfordNERTagger(model_filename=modelfile, path_to_jar=jarfile)
        tokenized_text = word_tokenize(self.text)
        classified_text = st.tag(tokenized_text)

        #return organization names
        regexNN = re.compile('ORGANIZATION')
        org_list = list()
        i = 0
        while i < len(classified_text):
            print (i)
            item = classified_text[i]
            if regexNN.search(item[1]):
                n = i + 1
                company = item[0]

                while n < len(classified_text):
                    item = classified_text[n]
                    if regexNN.search(item[1]):
                        company = company +" "+ item[0]
                        n = n +1
                    else:
                        break
                i = n
                org_list.append(company)
            i = i + 1

        return org_list