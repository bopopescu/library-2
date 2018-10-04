from bs4 import BeautifulSoup

# input html file, output plain text file
import re

class ParseHTML:

    def __init__(self, path):
        self.path = path
        with open(path, 'r') as my_file:
            html = my_file.read()

            parsed_html = BeautifulSoup(html, "lxml")
            text = parsed_html.getText()

            page = open('/home/gtohill/Desktop/parsed_file', 'w')
            lines = re.split('\n' or '[\\p{Punct}\\s]+' or '\p{Punct}', text)

            for line in lines:
                page.write(line.encode('UTF-8', 'ignore').lower()+'\n')

            page.close()
            self.file_path = page.name

    # get the file path to the text file containing the parsed html to text
    def get_file_path(self):
        return self.file_path

    # end of code
