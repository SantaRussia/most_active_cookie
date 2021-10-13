#!/usr/bin/python


import sys, getopt
import csv

'''
Shan Hao

Command: python most_active_cookie.py cookie_log.csv -d 2018-12-08

Test Commands: 
python most_active_cookie.py cookie_log.csv -d 2018-12-07
python most_active_cookie.py cookie_log.csv -d 2018-12-08
python most_active_cookie.py cookie_log.csv -d 2018-12-09
python most_active_cookie.py cookie_log.csv -d 2000-12-08
python most_active_cookie.py cookie_log.csv -d 2500-12-08
python most_active_cookie.py cookie_log.csv -d 2018-02-29
python most_active_cookie.py cookie_log.csv -d 2500-11-31
python most_active_cookie.py cookie_log.csv -d 2018-1-4
python most_active_cookie.py cookie_log.csv -d adfjoe
python most_active_cookie.py cookie_log.csv -d 
python most_active_cookie.py cookie_log.csv
python most_active_cookie.py cookie_log.cs
python most_active_cookie.py cook
python most_active_cookie.py file.csv -d 2018-12-08
python most_active_cookie.py
python most_active_cookie.py -d 2020-03-05-09
empty file
'''

# Judge whether a date is valid
def date_is_valid(s):
    try:
        year, month, day = s.split('-')
        if len(year) != 4 or len(month) != 2 or len(day) != 2 or int(year) < 0:
            return False
        days = ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']
        min_day = '01'
        max_day = ''

        # Get the maximum date in the month
        if 1 <= int(month) <= 12:
            max_day = days[int(month) - 1]
        if month == '02':
            if (int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 100 == 0 and int(year) % 400 == 0):
                max_day = '29'
        if not max_day or day < min_day or day > max_day:
            return False
        return True
    except ValueError:
        return False


def main(argv):
    input_date = ''
    filename = ''

    # Analyze the command.
    try:
        opts, args = getopt.getopt(argv, "")
    except getopt.GetoptError:
        print('python main.py <filename.csv> -d <yyyy-mm-dd>')
        sys.exit(2)

    # Get the date.
    for i in range(len(args)):
        if args[i] == "-d":
            if i == len(args) - 1:
                print('python main.py <filename.csv> -d <yyyy-mm-dd>')
                sys.exit(2)
            input_date = args[i + 1]
        # Get the file name. The file should be a csv file.
        elif '.csv' == args[i][-4:]:
            filename = args[i]
    if filename == '' or not date_is_valid(input_date):
        print('python main.py <filename.csv> -d <yyyy-mm-dd>')
        sys.exit(2)
    # print('input_date: ', input_date)
    # print('filename: ', filename)

    # Read the input csv file. 
    try:
        csv_reader = list(csv.reader(open(filename)))
        # If the date not in the file, we do not need to go in the iteration.
        max_date = csv_reader[1][1].split('T')[0]
        min_date = csv_reader[-1][1].split('T')[0]
        if input_date > max_date or input_date < min_date:
            return
        # cookie_dic {cookie: count}
        cookie_dic = {}
        # Time consumption: O(k)~O(n) n is the amount of line in the file. k is the number of
        # different cookies in the input day
        for line in csv_reader[1:]:
            # Get the cookie and the date of a line.
            cookie, date_time = list(line)
            date = date_time.split('T')[0]

            # Generate the dictionary.
            if date == input_date:
                if cookie in cookie_dic:
                    cookie_dic[cookie] += 1
                else:
                    cookie_dic[cookie] = 1
            elif date < input_date:
                break
        # print(cookie_dic)
        ans = []

        # Get the maximum cookies of the input date. Time consumption: O(k) (k is the number of different cookies in
        # the input day).
        max_val = max(cookie_dic.values())
        # print("max_val", max_val)
        for key in cookie_dic:
            if cookie_dic[key] == max_val:
                ans.append(key)

        #Print the answer.
        for s in ans:
            print(s)
    except FileNotFoundError:
        print("File Not Found.")


if __name__ == "__main__":
    main(sys.argv[1:])
