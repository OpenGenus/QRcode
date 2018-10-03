import re
from mode import (
    get_mode,
    NUMERIC,
    ALPHA_NUMERIC
)

from utils import (
    data_encode
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
    def encode(self):
        if self.mode == NUMERIC:
            pass
        else:
            print("Encoding.....")
            pairs_list = re.findall('..?',self.data) # separates in pair.
            data = data_encode(pairs_list,len(self.data))
            print(data)
