
class Channel:
    def __init__(self, channel_no, channel_label, MFCCs):
        self.channel_no = channel_no
        self.channel_label = channel_label
        self.MFCCs = MFCCs
        
class EEG:
    def __init__(self, subject, class_nr, class_label, channels):
        
        self.subject = subject
        self.class_nr = class_nr
        self.class_label = class_label
        self.channels = channels
        