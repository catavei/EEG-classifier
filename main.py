import csv
import statistics 
import numpy as np
import matplotlib.pyplot as plt
from EEG import EEG, Channel


NO_OF_MFCCS = 18
NO_OF_CHANNELS = 62
NO_OF_EEGS = 993
NO_OF_GAUSSIAN_EEGS = int(0.3*NO_OF_EEGS)


def create_initial_EEGs(raw_input):
    data_in = raw_input[1:, 1:30]

    tables_array = np.split(data_in, NO_OF_EEGS)
    
    EEGs = []
    
    for table in tables_array:
        
        subject = str(table[0, 0])
        class_nr = int(table[0, 2])
        class_label = str(table[0, 3])
        channels = []
        
        for i in range(NO_OF_CHANNELS):
            
            channel_label = str(table[i,5])
            MFCCs = table[i, 11:]
            MFCC_list = []
            
            for j in range(NO_OF_MFCCS):
                MFCC_list.append(float(MFCCs[j]))
                
            channel = Channel(i, channel_label, MFCC_list)
            channels.append(channel)
        
        EEGs.append(EEG(subject, class_nr, class_label, channels))
    
    return EEGs


def get_gaussian_params(MFCC_tables):
    
    MFCC_tables = np.array(MFCC_tables)
    mus = np.zeros((NO_OF_CHANNELS, NO_OF_MFCCS))
    sigmas = np.zeros((NO_OF_CHANNELS, NO_OF_MFCCS))
    
    for i in range(NO_OF_CHANNELS):
        for j in range(NO_OF_MFCCS):
            mus[i][j] = sum(MFCC_tables[:,i,j])/NO_OF_EEGS
            sigmas[i][j] = statistics.stdev(MFCC_tables[:,i,j])
    
    return mus, sigmas


def get_MFCC_tables(EEGs):
    
    MFCC_tables = []
    
    for EEGx in EEGs:
        
        MFCC_table = []
        
        for channel in EEGx.channels:
            MFCC_table.append(channel.MFCCs)
            
        MFCC_tables.append(MFCC_table)
    
    return MFCC_tables


def generate_gaussian_EEGS(mus, sigmas):
    
    generated_EEGs = np.zeros((NO_OF_GAUSSIAN_EEGS, NO_OF_CHANNELS, NO_OF_MFCCS))
    
    for i in range(NO_OF_CHANNELS):
        for j in range(NO_OF_MFCCS):
            generated_EEGs[:,i,j] = np.random.normal(mus[i,j], sigmas[i,j], NO_OF_GAUSSIAN_EEGS)
            
            
    return generated_EEGs
    
    
reader = csv.reader(open("input_data.csv"), delimiter=",")
raw_input = np.array(list(reader))


EEGs = create_initial_EEGs(raw_input)

MFCC_tables = get_MFCC_tables(EEGs)
MFCC_tables = np.array(MFCC_tables)

mus, sigmas = get_gaussian_params(MFCC_tables)
        
gaussian_EEGs = generate_gaussian_EEGS(mus, sigmas)



x = list(MFCC_tables[:,0,0])

hist = np.histogram(x, bins=100)
plt.plot(hist[0])
plt.show()

y = list(gaussian_EEGs[:,0,0])
hist = np.histogram(y, bins = 100)
plt.plot(hist[0])
plt.show()
    

del reader

