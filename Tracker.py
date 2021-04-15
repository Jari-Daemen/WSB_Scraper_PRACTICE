# Counts the amount of mentions of a certain ticker

import requests as r
import bs4 as bs



active = True
comments = []
while active:
    source = r.get('''
    https://www.reddit.com/r/wallstreetbets/comments/mrbmfj/daily_discussion_thread_for_april_15_2021/'''
                   ).text

    soup = bs.BeautifulSoup(source, features='html.parser')

    match = soup.find('div', class_="_3tw__eCCe7j-epNCKGXUKk")
    if match == None:
        continue
    else:
        comment = str(match.find('p', class_="_1qeIAgB0cPwnLhDF9XSiJM"))
        comment = comment [35:-4]

        if comment in comments:
            continue
        else:
            comments.append(comment)
            print(comment)



