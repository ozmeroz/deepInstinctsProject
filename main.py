from functions import *
a_file = open("shiftReport.txt", "r")  # input report file
reportLines = [(line.strip()).split() for line in a_file]  # generate report file into list by lines
a_file.close()  # close file

guardset = set({}) # use Set to avoid duplicate guard numbers, represents guard number of all guards in report file
shift,guardset = shiftSummary(reportLines,guardset)  # create list of processed data from file and guard numbers set
countPerGuard = sleepSum(shift,guardset)
sleeper = findSleeper(countPerGuard)
estimatedTime= findTime(shift,sleeper)
print("Guard #"+sleeper + " is most likely to be asllep in 00:"+estimatedTime)




