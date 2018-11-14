from mode import (
    NUMERIC,
    ALPHA_NUMERIC,
    BYTE,
    KANJI
)
def mode_indicator(mode):
    if mode==ALPHA_NUMERIC:
        return '0010'
    elif mode==NUMERIC:
        return '0001'
    elif mode==BYTE:
        return '0100'
    else:
        return '1000'

def char_count_indicator(version,mode,data_len):
    binary = '{0:b}'.format(data_len)
    if(1<=version<=9):
        if(mode==ALPHA_NUMERIC):
            while(len(binary)!=9):
                binary = '0'+binary
        elif(mode == NUMERIC):
            # make binary 10 bits with 0 left padded for numeric
            while(len(binary)!=10):
                binary = '0'+binary
        elif(mode == BYTE):
            # make binary 8 bits with 0 left padded for byte
            while(len(binary)!=8):
                binary = '0'+binary
        else:
            while(len(binary)!=8):
                binary = '0'+binary
    elif(10<=version<=26):
        if(mode==ALPHA_NUMERIC):
            while(len(binary)!=11):
                binary = '0'+binary
        elif(mode == NUMERIC):
            # make binary a 12 bit for numeric
            while(len(binary)!=12):
                binary = '0'+binary
        elif(mode == BYTE):
            # make binary 16 bits with 0 left padded for byte
            while(len(binary)!=16):
                binary = '0'+binary
        else:
            while(len(binary)!=10):
                binary = '0'+binary
    else:
        if(mode==ALPHA_NUMERIC):
            while(len(binary)!=13):
                binary = '0'+binary
        elif(mode == NUMERIC):
            #make binary 14bit for numeric
            while(len(binary)!=14):
                binary = '0'+binary
        elif(mode == BYTE):
            # make binary 16 bits with 0 left padded for byte
            while(len(binary)!=16):
                binary = '0'+binary
        else:
            while(len(binary)!=12):
                binary = '0'+binary
    return binary