import re

def caesar_cipher(string, shift_amount):
    alpha_low = 'abcdefghijklmnopqrstuvwxyz'
    alpha_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    i = 0
    upper_case = False
    while i < len(string):
        str_char = str(string[i])
        #print(str_char)
        if re.match("[a-z]", str_char):
            letter_index = alpha_low.find(str_char) 
            result.append(letter_index)
        elif re.match("[A-Z]", str_char):
            letter_index = alpha_up.find(str_char) 
            result.append(letter_index)
        elif re.match("[^a-zA-Z]", str_char):
            result.append(str_char)           
        i += 1

    return result

print(caesar_cipher("What a string!", 5))

        # if re.match("[^a-zA-Z]", string[i]):
        #     result.append(string[i])
        #     i += 1
        # else:
        #     re.match("[a-z]", string[i])
        #     lower_case = True
        #     letter_index = alpha_low.index(string[i])
        #     print(letter_index)
        #     i += 1