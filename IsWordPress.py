import requests


def isThisWordPress(url):
    r = requests.get(url)
    html_documument = r.text.lower()

    word_press_site = ['wordpress', 'wp-content']
    # store boolean value if wp site is found
    found_wp =''
    for word in word_press_site:
        is_word_press = word in html_documument
        if is_word_press:
            return True
        else:
            found_wp = False

    return found_wp


wp_site = isThisWordPress('http://www.oxfordconnection.ca/')
print(wp_site)