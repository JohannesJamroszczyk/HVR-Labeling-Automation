from linkerFileCreation import *
from formattingTools import *

label_file = mk_text_file("Label Files/label1.lbl")
config_file = mk_text_file("Label Files/config.cfg")

df = csv_to_matrix("testData.csv")

configMatrix = popped_matrix(df, 0)

#lable_file.write("This is a labelFile")
config_file.write(matrix_to_config(configMatrix))


