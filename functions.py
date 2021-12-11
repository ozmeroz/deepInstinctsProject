import tkinter
from tkinter import messagebox
import sys
# This code is to hide the main tkinter window
root = tkinter.Tk()
root.withdraw()

# assuming the report file is based on one hour only(between 12-1 there is only one guard)

def shiftSummary(reportLines, guardset):
    """function that gets reportLines list and set varriable of guard number who worked in the report file \
    and returns shift summery list and updated guardSet(Set) with all guard numbers"""
    shift = []
    for line in reportLines:
        if len(line) == 6:  # if list length of line has 6 indexes - guard registration to shift report
            currentGuardNum = line[3][1:]     # get guard number without "#" sign
            if not currentGuardNum.isnumeric():
                raise ValueError("Guard number not in supported format! please check the file")
            guardset.add(currentGuardNum)   # update set with guard numbers - set will ignore duplicates
        elif len(line) == 4:  # if list length of the line has 4 indexes - sleep or wake report
            if line[3] == "asleep":
                fallTime = line[1][3:5]   # takes only minute varriable of the report line
            elif line[2] == "wakes":
                wakeTime = line[1][3:5]   # takes only minute varriable of the report line
                # update list with guard number, fall asleep minute, wakeup minute, and sleep length in minutes
                shift.append([currentGuardNum, fallTime, wakeTime, int(wakeTime) - int(fallTime)])
        else:
            if len(line) != 6 or len(line) != 4:
                print("Unsupported format line on report file!")
            if messagebox.askokcancel("Unsupported format", "Please press OK and choose supported format report file! \n if you choose cancel program will check next line report and discard wrong format line."):
                raise Exception("Unsupported format line on report file!")  # Exception will be raised if user click OK
            else:
                continue  # will discard iteration and continue with next line on report
    return shift, guardset


def sleepSum(shift, guardset):
    """function that gets shift report list and returns list of lists with guard numbers and sum of sleep time"""
    """in case of zero sleep time report file - will return False"""
    sign = False
    countPerGuard = []
    for i in guardset:
        count = 0
        for data in shift:
            if data[0] == i:
                count += data[3]
        if count!=0:
            sign = True
        countPerGuard.append([i, count])
    if sign == False:
        return False
    return countPerGuard


def findSleeper(countPerGuard):
    """function that gets countPerGuard list and returns the Guard number who slept the most time
    if 2 or more guards slept the same amount of minutes - will return the last one from them as he worked last
    if no sleeper in report - will return False"""
    if countPerGuard == False:
        return False
    maxsleeptime = 0
    sleeper = countPerGuard[0][0]
    for i in countPerGuard:
        if i[1] >= maxsleeptime:
            maxsleeptime = i[1]
            sleeper = i[0]
    return sleeper


# check which time he is most likely to be asleep
def findTime(shift, sleeper):
    """function that gets shiftSummary list and sleeper guard number and returns estimated time of sleep
    if no sleeper found -function will return False"""
    if sleeper == False:
        return False
    minutes = []
    for i in range(60):
        minutes.append(0)  # generates a list with length of 60 indexes, each index will represent a minute
    for i in shift:
        if i[0] == sleeper:  # connects the check to the relevant sleeper guard
            for x in range(int(i[1]), int(i[2])):
                minutes[x] += 1

    estimated = minutes.index(max(minutes))
    if estimated >= 0 and estimated <= 9:
        estimated = "0" + str(estimated)
    else:
        estimated = str(estimated)
    return estimated
