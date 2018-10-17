from qrcode.mode import (
    NUMERIC,
    ALPHA_NUMERIC
)
def mode_indicator(mode):
    if(mode==ALPHA_NUMERIC):
        return '0010'
    else:
        return '0001'
def char_count_indicator(version,mode,data_len):
    binary = '{0:b}'.format(data_len)
    if(1<=version<=9):
        if(mode==ALPHA_NUMERIC):
            while(len(binary)!=9):
                binary = '0'+binary
        else:
            # make binary 10 bits with 0 left padded for numeric
            pass
    elif(10<=version<=26):
        if(mode==ALPHA_NUMERIC):
            while(len(binary)!=11):
                binary = '0'+binary
        else:
            # make binary a 12 bit for numeric
            pass
    else:
        if(mode==ALPHA_NUMERIC):
            while(len(binary)!=13):
                binary = '0'+binary
        else:
            #make binary 14bit for numeric
            pass
    return binary