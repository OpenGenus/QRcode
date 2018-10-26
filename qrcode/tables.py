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
            (41,25,17),
            (34,20,14),
            (27,16,11),
            (17,10,7)
        ],
        [
            (77,47,32),
            (63,38,26),
            (48,29,20),
            (34,20,14)
        ],
        [
            (127,77,53),
            (101,61,42),
            (77,47,32),
            (58,35,24)
        ] 
    ]
    return capacity_table
