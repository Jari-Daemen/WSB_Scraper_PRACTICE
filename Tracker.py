# Counts the amount of mentions of a certain ticker

import requests as r
import bs4 as bs
import re
from collections import  Counter
from datetime import datetime

active = True
comments = []
sub = []
tickers = []

while active:

    # source and class may need to be adjusted (automatically)

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



                time = str(datetime.now())
                print(time)
                if time == '2021-04-15 23:20:00.000000':
                    final_list = sorted(occurences.items(), key=lambda x: int(x[0]))
                    final_list = sorted(final_list, reverse=True)
                    print(final_list)
                    break

#prints the final list of tuples in descending key value



    #final_list = sorted(occurences.items(), key=lambda x: int(x[0]))
    #final_list = sorted(final_list, reverse=True)
    #print(final_list)