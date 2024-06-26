# HackerRank - Algorithms
# Time Conversion
# By Douglas Horville

# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

import re

def timeConversion(s):
    print("Original string:", s)
    # isolate AM/PM and remove from string, and split string into hours, minutes and seconds
    am_pm = s[-2:]
    string = s.replace(am_pm, '')
    times = string.split(':')
    [hh, mm, ss] = [times[0], times[1], times[2]]
    print(f"Hours = {hh}, Minutes = {mm}, Seconds = {ss}, and it is {am_pm}")
    
    if am_pm == 'AM' and hh == '12':  # AM logic
        hh = '00'    
    elif am_pm == 'PM' and int(hh) < 12:  # PM logic
        # if hh == '12':
        #     hh = '12'
        hh = int(hh) + 12
    return f"{hh}:{mm}:{ss}"




def main():
    # print(timeConversion('07:05:45PM'))
    # print(timeConversion('12:05:45AM'))
    print(timeConversion('12:45:54PM'))

main()