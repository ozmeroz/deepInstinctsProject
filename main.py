from functions import *
from FileScan import *
# to scan file, please create FileScan object with file name with extension if in folder
# user can also provide file including path if not in project folder.
# please activate each file separately to see all scenarios - just delete comment mark '#'
#  user can choose multiple files to scan - just create FileScan Object for each file you want to scan.
# "shiftReport.txt" Represents the file given in challenge doc file as is.
# "shiftReport2.txt" and "shiftReport3.txt" are just other valid scenarios to check my code.
# "shiftReport4.txt" Represents report with wrong format line - run and check it out
# "shiftReport5.txt" Represents report with multiple wrong format lines - run and check it out


f1 = FileScan("Report files/shiftReport.txt")  # valid file given by DeepInstinct
# localfile = FileScan("C:/users/ozmer/Desktop/shiftReport.txt")  #  will work only in my local comp
# f2 = FileScan("Report files/shiftReport2.txt")
# f3 = FileScan("Report files/shiftReport3.txt")
# f4 = FileScan("Report files/shiftReport4.txt")
# f5 = FileScan("Report files/shiftReport5.txt")
# f6 = FileScan("Report files/shiftReport6.txt")  # one guard number only
# f7 = FileScan("Report files/shiftReport7.txt")  # 2 equal sleep time - will give last worker who worked with same amount of minutes slept
# f8 = FileScan("Report files/shiftReport8.txt")  # no sleeper guard on report
# f9 = FileScan("Report files/shiftReport9.txt")  # invalid guard number on report


