from linkerFileCreation import *
from formattingTools import *

timeIndex = 0

lableName = "label.lbl"
configName = "config.lbl"

label_file = mk_text_file(f"Label Files/{lableName}")
config_file = mk_text_file(f"Label Files/{configName}")

dataframe = csv_to_matrix("testData.csv")

timeArr = get_date_time(dataframe, timeIndex)
datMatrix = popped_matrix(dataframe, timeIndex)

date = get_date(timeArr, datMatrix)
time = get_time(timeArr, datMatrix)

version = 101

print(matrix_to_label(datMatrix, time, interval_time(time, 10), date, version, lableName))

# config_file.write(matrix_to_config(datMatrix))
