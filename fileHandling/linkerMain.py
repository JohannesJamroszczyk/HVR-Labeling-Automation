from linkerFileCreation import *
from formattingTools import *
import pandas as pd


label_file = mk_text_file("Label Files/label1.lbl")
config_file = mk_text_file("Label Files/config.cfg")

df = csv_to_matrix("testData.csv")

print(df)

#lable_file.write("This is a labelFile")
config_file.write(matrix_to_config(df))


