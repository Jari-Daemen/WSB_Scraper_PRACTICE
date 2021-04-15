# Counts the amount of mentions of a certain ticker

import requests as r
import bs4 as bs

source = r.get('''
https://www.reddit.com/r/wallstreetbets/comments/mrbmfj/daily_discussion_thread_for_april_15_2021/'''
               ).text

soup = bs.BeautifulSoup(source, features='html.parser')

match = soup.find('div', class_="_3tw__eCCe7j-epNCKGXUKk")

print(match)

#print(comment)
#comment = match.find('p', class_="_1qeIAgB0cPwnLhDF9XSiJM")
