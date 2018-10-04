from parse_html import *


class SEOKeywords:

    def __init__(self, fle, kywds):
        self.file = fle
        self.keywords = kywds

    def search_keywords(self):
        found = list()
        file = open(self.file, 'r')
        read_lines = file.read()
        lines = read_lines.split('\n' or '[\\p{Punct}\\s]+') # put lines from text file in list

        for word in self.keywords:
            for line in lines:
                if word in line:
                    found.append((word, line))

        return found


if __name__ == '__main__':
    from parse_html import *

    path_to_html_file = '/home/gtohill/Desktop/parse_html.html'
    path_to_text_file = ParseHTML(path_to_html_file).get_file_path()
    keywords = input("Enter SEO Keywords: ")
    each_word = re.split('[\s]', keywords)

    found = SEOKeywords(path_to_text_file, each_word).search_keywords()
    #print(found)
    for f in found:
        print(f)

