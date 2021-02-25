from linkerFileCreation import *
from formattingTools import *

timeIndex = 0

label_file = mk_text_file("Label Files/label1.lbl")
config_file = mk_text_file("Label Files/config.cfg")

dataframe = csv_to_matrix("testData.csv")

timeArr = get_date_time(dataframe, timeIndex)
datMatrix = popped_matrix(dataframe, timeIndex)

date = get_date(timeArr, datMatrix)
time = get_time(timeArr, datMatrix)

print(date)
print(time)

# config_file.write(matrix_to_config(datMatrix))
