from linkerFileCreation import *
from formattingTools import *

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# These are the things that need to be indicated by the user

timeIndex = 2
intervalMins = 10
lableFileName = "label.lbl"
configFileName = "label.cfg"
lableVersion = 101
csvFileLocation = "test.csv"


DamsStartTime = "12:48:59"
DamsStartDate = "24-01-21"
DamsEndTime = "00:58:53"
DamsEndDate = "25-01-21"

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

DamsStart = f"{DamsStartDate}/{DamsStartTime}"
DamsEnd = f"{DamsEndDate}/{DamsEndTime}"

label_file = mk_text_file(f"Label Files/{lableFileName}")
config_file = mk_text_file(f"Label Files/{configFileName}")

dataFrame = csv_to_matrix(csvFileLocation)

timeArr = get_date_time(dataFrame, timeIndex)
print(timeArr)
datMatrix = popped_matrix(dataFrame, timeIndex)
print(datMatrix)
labelsNumbers = labelList(datMatrix)
print(labelsNumbers)
date = get_date(timeArr, datMatrix)
print(date)
time = get_time(timeArr, datMatrix)
print(time)

label_file.write(matrix_to_label(labelsNumbers, datMatrix, time, interval_time(time, intervalMins), date, lableVersion,
                                 lableFileName, DamsStart, DamsEnd))

config_file.write(matrix_to_config(datMatrix))
