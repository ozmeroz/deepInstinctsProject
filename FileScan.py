from functions import *


class FileScan:
    def __init__(self, filename):  # constructor
        self.filename = filename
        if type(filename) == str and filename != '':
            if filename.endswith(".txt"):
                self.filename = filename
            else:
                raise ValueError("Please fill file name with extension(.txt)")
        else:
            raise ValueError('File name is not valid or empty!')
        self.a_file = open(self.filename, "r")  # input report file
        self.reportLines = [(line.strip()).split() for line in self.a_file]  # generate report file into list by lines
        self.a_file.close()  # close file
        # use Set to avoid duplicate guard numbers, represents guard number of all guards in report file
        self.guardset = set({})
        self.shift, self.guardset = shiftSummary(self.reportLines, self.guardset)  # create list of processed data from file and guard numbers set
        self.countPerGuard = sleepSum(self.shift, self.guardset)
        self.sleeper = findSleeper(self.countPerGuard)
        self.estimatedTime = findTime(self.shift, self.sleeper)
        if self.estimatedTime!=False:
            print("File report:\nGuard #" + self.sleeper + " is most likely to be asleep in 00:" + self.estimatedTime)
        else:
            print("No sleeper found on report file.")

