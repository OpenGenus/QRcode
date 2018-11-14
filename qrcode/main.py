import re
from mode import (
    get_mode,
    NUMERIC,
    ALPHA_NUMERIC,
    BYTE,
    KANJI
)

from utils import (
    data_encode,
    numeric_encode,
    byte_encode,
    kanji_encode,
    get_version_and_capacity
)

from constants import (
    mode_indicator,
    char_count_indicator
)

class QRCODE:
    def __init__(self):
        self.data = ''
        self.mode = ''
        self.version = 0
        self.capacity = 0
        self.level = ''
    def __str__(self):
        return self.data + " " + self.mode
    def create(self,data):
        self.data = data
        self.mode = get_mode(data)
        self.determine_version()
        self.encode()

    def determine_version(self):
        data_length = len(self.data)
        ver_and_cap = get_version_and_capacity(data_length,self.mode)
        self.version = ver_and_cap[0]
        self.capacity = ver_and_cap[1]
        # self.level = ver_and_cap[2]
    def encode(self):
        if self.mode == NUMERIC:
            pairs_list = re.findall('.{1,3}', self.data)
            data = numeric_encode(pairs_list)

        elif self.mode == ALPHA_NUMERIC:
            pairs_list = re.findall('..?',self.data) # separates in pair.
            data = data_encode(pairs_list)

        elif self.mode == BYTE:
            data = byte_encode(self.data)
        else:
            data = kanji_encode(self.data)
        encoded_data = ''
        for each_encoded_data in data:
            encoded_data+=each_encoded_data
        mode_indicator_data = mode_indicator(self.mode)
        char_count_indicator_data = char_count_indicator(
                                        self.version,
                                        self.mode,
                                        len(self.data)
                                    )
        data_with_error = mode_indicator_data+ (
                char_count_indicator_data + 
                encoded_data
        )
        print(data_with_error)

