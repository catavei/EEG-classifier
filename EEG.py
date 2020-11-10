NO_OF_MFCCS = 18
NO_OF_CHANNELS = 62

class Channel:
    def __init__(self, channel_no, channel_label, MFCCs):
        self.channel_no = channel_no
        self.channel_label = channel_label
        self.MFFCs = MFCCs
        
class EEG:
    def __init__(self, input_table):
        
        self.subject = str(input_table[0, 0])
        self.class_nr = int(input_table[0, 2])
        self.class_label = str(input_table[0, 3])
        self.channels = []
        
        for i in range(NO_OF_CHANNELS):
            
            channel_label = str(input_table[i,5])
            MFCCs = input_table[i, 11:]
            MFCC_list = []
            
            for j in range(NO_OF_MFCCS):
                MFCC_list.append(float(MFCCs[j]))
                
            channel = Channel(i, channel_label, MFCC_list)
            self.channels.append(channel)