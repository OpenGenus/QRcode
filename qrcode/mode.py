import re
NUMERIC = 'NUMERIC'
ALPHA_NUMERIC = 'ALPHA-NUMERIC'
BYTE = 'BYTE'
KANJI = 'KANJI'

def get_mode(data):
    for n in re.findall('[\u4e00-\u9fff]+',data):
        return KANJI
    flag = 1
    byte = re.search("[^a-zA-Z0-9]+", data)
    if (byte):
        return BYTE
    for each in data:
        if not(each.isdigit()):
            flag = 0
    if flag:
        return NUMERIC
    elif flag==0:
        return ALPHA_NUMERIC
    