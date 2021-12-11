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
            currentGuardNum=line[3][1:]     # get guard number without "#" sign
            guardset.add(currentGuardNum)   # update set with guard numbers - set will ignore duplicates
        elif len(line) == 4:  # if list length of the line has 4 indexes - sleep or wake report
            if line[3] == "asleep":
                fallTime=line[1][3:5]   # takes only minute varriable of the report line
            elif line[2] == "wakes":
                wakeTime=line[1][3:5]   # takes only minute varriable of the report line
                # update list with guard number, fall asleep minute, wakeup minute, and sleep length in minutes
                shift.append([currentGuardNum, fallTime, wakeTime, int(wakeTime) - int(fallTime)])
        else:
            if len(line)!= 6 or len(line)!=4 :
                print("Unsupported format line on report file!")
            if messagebox.askokcancel("Unsupported format", "Please press OK and choose supported format report file! \n if you choose cancel program will check next line report and discard wrong format line."):
                sys.exit() # will stop script from running with wrong format
            else:
                continue # will discard iteration and continue with next line on report
    return shift,guardset


def sleepSum(shift, guardset):
    """function that gets shift report list and returns list of lists with guard numbers and sum of sleep time"""
    countPerGuard=[]
    for i in guardset:
        count=0
        for data in shift:
            if data[0]==i:
                count+=data[3]
        countPerGuard.append([i , count])
    return countPerGuard


def findSleeper(countPerGuard):
    """function that gets countPerGuard list and returns the Guard number who slept the most time"""
    maxsleeptime=0
    sleeper=countPerGuard[0][0]
    for i in countPerGuard:
        if i[1]>=maxsleeptime:
            maxsleeptime=i[1]
            sleeper=i[0]
    return sleeper


# check which time he is most likely to be asleep
def findTime(shift, sleeper):
    """function that gets shiftSummary list and sleeper guard number and returns estimated time of sleep"""
    minutes = []
    for i in range(60): minutes.append(0) # generate list with length of 60, each index will present a minute
    for i in shift:
        if i[0] == sleeper:
            for x in range(int(i[1]), int(i[2])):
                minutes[x] += 1

    estimated = minutes.index(max(minutes))
    if estimated >= 0 and estimated <= 9:
        estimated = "0" + str(estimated)
    else:
        estimated = str(estimated)
    return estimated
