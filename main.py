import csv
import numpy as np
from EEG import EEG

reader = csv.reader(open("input_data.csv"), delimiter=",")

raw_input = np.array(list(reader))
data_in = raw_input[1:, 1:30]

tables_array = np.split(data_in, data_in.shape[0]/62)

EEGs = []

for table in tables_array:
    EEGs.append(EEG(table))
    
del tables_array, table, reader, data_in, raw_input



    