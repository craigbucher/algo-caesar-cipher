import re

def caesar_cipher(string, index):
    alpha_low = 'abcdefghijklmnopqrstuvwxyz'
    alpha_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    i = 0
    upper_case = False
    while i < len(string):
        str_char = str(string[i])
        if re.match("[a-z]", str_char):
            letter_index = alpha_low.find(str_char)
            if (letter_index + index) < 0:
                letter_index += 26
                result.append(alpha_low[letter_index + index])
            elif (letter_index + index) > 26:
                letter_index -= 26
                result.append(alpha_low[letter_index + index])
            else:
                result.append(alpha_low[letter_index + index])
        elif re.match("[A-Z]", str_char):
            letter_index = alpha_up.find(str_char) 
            if (letter_index + index) < 0:
                letter_index += 26
                result.append(alpha_up[letter_index + index])
            elif (letter_index + index) > 26:
                letter_index -= 26
                result.append(alpha_up[letter_index + index])
            else:
                result.append(alpha_up[letter_index + index])
        elif re.match("[^a-zA-Z]", str_char):
            result.append(str_char)           
        i += 1

    return ''.join(result)

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