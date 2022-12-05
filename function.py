from random import randint

num_signs= "1234567890@&?!<>#%^*"
chars_up = "QWERTYUIOPASDFGHJKLZXCVBNM"
chars_low = "qwertyuiopasdfghjklzxcvbnm"


def generate(num_signs:str, char_up:str, char_low:str)->str:
    for i in range(0, 16):
        r_s = randint(0, len(num_signs)-1)
        r_u = randint(0, len(chars_up)-1)
        r_l = randint(0, len(chars_low)-1)
        j = randint(0, 2)
        if j == 0:
            generate += num_signs[r_s]
        elif j == 1:
            generate += chars_up[r_u]
        else:
            generate += chars_low[r_l]
    return generate