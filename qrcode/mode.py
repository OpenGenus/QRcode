import re
NUMERIC = 'NUMERIC'
ALPHA_NUMERIC = 'ALPHA-NUMERIC'
BYTE = 'BYTE'

def get_mode(data):
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