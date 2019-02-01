from collections import Counter
import operator


def anagramchk(word, chkword):
    for letter in word:
        if letter in chkword:
            chkword = chkword.replace(letter, '', 1)
        else:
            return 0
    return 1


def sherlockAndAnagrams(s):


    for i in s:
        hashdict = Counter()
        salist = list()
        x = 0
        #front = ''

        while x < len(i):
            front = i[x]
            hashdict.update({front})
            #salist.append((front, len(front)))
            y = x + 1
            #next = ''
            while y < len(i):
                next = i[y]
                front += next
                hashdict.update({front})
                #salist.append((front, len(front)))
                y += 1

            x += 1

        # sorted_x = sorted(salist, key=operator.itemgetter(1))
        print(hashdict)
        '''
        count = 0
        for x in range(0, len(hashdict)-1):
            for y in range(x, len(hashdict)-1):
                y = y + 1
                t1 = salist[x][0]
                t2 = salist[y][0]
                if len(t1) == len(t2):
                    count += anagramchk(t1, t2)

        print("Count: ", count)
        '''
s = ['kkkk']
'''
#s = ['ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel',
     'gffryqktmwocejbxfidpjfgrrkpowoxwggxaknmltjcpazgtnakcfcogzatyskqjyorcftwxjrtgayvllutrjxpbzggjxbmxpnde',
     'mqmtjwxaaaxklheghvqcyhaaegtlyntxmoluqlzvuzgkwhkkfpwarkckansgabfclzgnumdrojexnrdunivxqjzfbzsodycnsnmw',
     'ofeqjnqnxwidhbuxxhfwargwkikjqwyghpsygjxyrarcoacwnhxyqlrviikfuiuotifznqmzpjrxycnqktkryutpqvbgbgthfges',
     'zjekimenscyiamnwlpxytkndjsygifmqlqibxxqlauxamfviftquntvkwppxrzuncyenacfivtigvfsadtlytzymuwvpntngkyhw',
     'ioqfhajbwdfnudqfsjhikzdjcbdymoecaokeomuimlzcaqkfmvquarmvlnrurdblzholugvwtkunirmnmsatrtbqlioauaxbcehl',
     'kaggklnwxoigxncgxnkrtdjnoeblhlxsblnqitdkoiftxnsafukbdhasdeihlhfrqkfzqhvnsmsgnrayhsyjsniutmgpfjmssfsg',
     'fhithnigqftuzzgpdiquhlsozksxxfreddmsmvqgfgzntphmgggszwtkcbmjsllwtukgqvpvxvmatuanbeossqwtpgzbagaukmta',
     'rqjfiszbigkdqxkfwtsbvksmfrffoanseuenvmxzsugidncvtifqesgreupsamtsyfrsvwlvhtyzgjgnmsowjwhovsmfvwuniasw',
     'dxskilnpkkdxwpeefvgkyohnwxtrrtxtckkdgnawrdjtcpzplywyxmwtemwmtklnclqccklotbpsrkazqolefprenwaozixvlxhu']
'''
sherlockAndAnagrams(s)
