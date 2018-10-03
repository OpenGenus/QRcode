from tables import (
    get_alphabet_table,
    char_capacity_table
)
alphabet_table = get_alphabet_table()
encoded_pairs = []
def data_encode(pairs_list,data_length):
    for pair in pairs_list:
        if len(pair) == 2:
            first = alphabet_table[pair[0]]
            second = alphabet_table[pair[1]]
            final = 45*first + second
            binary_final = '{0:b}'.format(final)
            ''' 
                padding the string with 0's to
                match the data length
            ''' 
            while(len(binary_final)!=data_length):
                binary_final = '0' + binary_final
        else:
            '''
            If you are encoding an odd number of characters,
            as we are here, take the numeric representation 
            of the final character and convert it into a 6-bit
            binary string.
            '''
            final = alphabet_table[pair[0]]
            binary_final = '{0:b}'.format(final)
            while(len(binary_final)!=6):
                binary_final = '0'+binary_final
        encoded_pairs.append(binary_final)    

        
    return encoded_pairs