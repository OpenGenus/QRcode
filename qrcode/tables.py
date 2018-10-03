def get_alphabet_table():
    alpha_table = {}
    for i in range(10):
        alpha_table[i] = i
    val = i+1
    for i in range(65,91):
        alpha_table[chr(i)] = val
        val+=1
    alpha_table[' '] = 36
    alpha_table['$'] = 37
    alpha_table['%'] = 38
    alpha_table['*'] = 39
    alpha_table['+'] = 40 
    alpha_table['-'] = 41
    alpha_table['.'] = 42
    alpha_table['/'] = 43
    alpha_table[':'] = 44
    return alpha_table

def char_capacity_table():
    capacity_table = [
        [
            ('L',41,25),
            ('M',34,20),
            ('Q',27,16),
            ('H',17,10),
        ],
        [
            ('L',77,47),
            ('M',63,38),
            ('Q',48,29),
            ('H',34,20),
        ],
        [
            ('L',127,77),
            ('M',101,61),
            ('Q',77,47),
            ('H',58,35),
        ], 
    ]
    return capacity_table
