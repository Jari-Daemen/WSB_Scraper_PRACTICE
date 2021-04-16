# Counts the amount of mentions of a certain ticker

import requests as r
import bs4 as bs
import re
from collections import Counter
from datetime import datetime
# from time import sleep
import os

active = True
comments = []
sub = []
tickers = []
skip = []
start_flag = True

# creating a text file containing the info

file_date = str(datetime.now())
file_date = file_date[0:10]

# specify a starting time for the program

while start_flag:
    start_time = str(datetime.now())
    start_time = start_time[11:16]

    if start_time == '12:08':
        print('The program has begun')
        start_flag = False

# The full loop

while active:

    time = str(datetime.now())
    time = time[11:16]

    # Specify a stopping time

    if time == '12:28':
        final_list = sorted(occurences.items(), key=lambda x: int(x[0]))
        final_list = sorted(final_list, reverse=True)
        print(final_list)
        print('The program has finished, storing results...')
        if os.path.isfile(f'Tickers {file_date}.txt'):
            print('File already exists!')
            break
        else:
            with open(f'Tickers {file_date}.txt', 'w') as docu:
                docu.write(final_list)
                break

    # source and class may need to be adjusted (automatically)

    # link has to be replaced every page, classes are constant

    source = r.get('''
    https://www.reddit.com/r/wallstreetbets/comments/mrzzt0/daily_discussion_thread_for_april_16_2021/'''
                   ).text

    soup = bs.BeautifulSoup(source, features='html.parser')
    match = soup.find('div', class_="_3tw__eCCe7j-epNCKGXUKk")

    #stickied = soup.find('span', class_="_2ETuFsVzMBxiHia6HfJCTQ _2wd-K5Djdc9TGPRGDgmkpX")
    #if stickied:
    #    tmp = str(match)
    #    tmp = tmp[1314:-4351]
    #    if tmp in sub:
    #        pass
    #    else:
    #        sub.append(tmp)
    #        print(sub)

    if match == None:
        continue

    #elif tmp in sub:
    #    print('loser')
    #    continue

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
