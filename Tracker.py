# Counts the amount of mentions of a certain ticker on WSB daily discussion thread

import requests as r
import bs4 as bs
import re
from collections import Counter
from datetime import datetime


active = True
comments = []
sub = []
tickers = []
start_flag = True

# specify a starting time for the program

while start_flag:
    start_time = str(datetime.now())
    start_time = start_time[11:16]

    if start_time == '14:32':
        print('The program has started')
        start_flag = False

# The full loop

while active:

    time = str(datetime.now())
    time = time[11:16]

    # Specify a stopping time

    if time == '14:36':

        final_list = sorted(occurences.items(), key=lambda x: (x[0])) #sorts amount of mentions from low to high
        print(final_list)
        print('The program has finished')
        break

    # link has to be replaced, classes are constant

    source = r.get('''
    https://www.reddit.com/r/wallstreetbets/comments/mrzzt0/daily_discussion_thread_for_april_16_2021/'''
                   ).text

    soup = bs.BeautifulSoup(source, features='html.parser')
    match = soup.find('div', class_="_3tw__eCCe7j-epNCKGXUKk")

    if match == None:
        continue

    else:
        comment = str(match.find('p', class_="_1qeIAgB0cPwnLhDF9XSiJM"))
        comment = comment[35:-4]

        if comment in comments or comment in sub:
            continue

        else:
            comments.append(comment)
            print(comment)

            for element in comments:
                a = re.compile(r'[A-Z]{2,5}')
                tmp = a.findall(element)
                comments.remove(comment)
                sub.append(comment)

                for ticker in tmp:
                    tickers.append(ticker)
                    occurences = Counter(tickers)


