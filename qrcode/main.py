import re
from mode import (
    get_mode,
    NUMERIC,
    ALPHA_NUMERIC
)

from utils import (
    data_encode,
    get_version_and_capacity
)

class QRCODE:
    def __init__(self):
        self.data = ''
        self.mode = ''
    def __str__(self):
        return self.data + " " + self.mode
    def create(self,data):
        self.data = data
        self.mode = get_mode(data)
        self.encode()
        self.determine_version()
    def encode(self):
        if self.mode == NUMERIC:
            pass
        else:
            print("Encoding.....")
            pairs_list = re.findall('..?',self.data) # separates in pair.
            data = data_encode(pairs_list)
            print(data)
    def determine_version(self):
        data_length = len(self.data)
        ver_and_cap = get_version_and_capacity(data_length,self.mode)
        print(ver_and_cap)
        
        
                    
