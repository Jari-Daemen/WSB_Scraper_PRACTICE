# Counts the amount of mentions of a certain ticker

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
    if start_time == '23:35':
        print('The program has begun')
        start_flag = False

# The full loop

while active:

    time = str(datetime.now())
    time = time[11:16]
    print(time)

    # Specify a stopping time

    if time == '23:42':
        final_list = sorted(occurences.items(), key=lambda x: int(x[0]))
        final_list = sorted(final_list, reverse=True)
        print(final_list)
        print('The program has finished')
        break

    # source and class may need to be adjusted (automatically)

    # link has to be replaced every page, classes are constant

    source = r.get('''
    https://www.reddit.com/r/wallstreetbets/comments/mrbmfj/daily_discussion_thread_for_april_15_2021/'''
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
                a = re.compile(r'[A-Z]{3,5}')
                tmp = a.findall(element)
                comments.remove(comment)
                sub.append(comment)

                for ticker in tmp:
                    tickers.append(ticker)
                    print(tickers)
                    occurences = Counter(tickers)
                    print(occurences)

# prints the final list of tuples in descending key value


# final_list = sorted(occurences.items(), key=lambda x: int(x[0]))
# final_list = sorted(final_list, reverse=True)
# print(final_list)
