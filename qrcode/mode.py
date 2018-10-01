NUMERIC = 'NUMERIC'
ALPHA_NUMERIC = 'ALPHA-NUMERIC'

def get_mode(data):
    flag = 1
    for each in data:
        if not(each.isdigit()):
            flag = 0
    if flag:
        return NUMERIC
    else:
        return ALPHA_NUMERIC