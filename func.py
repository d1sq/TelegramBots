from math import log2
def makeMeAString(arr, target_length=5, round_numbers=2, horizontal_char=' ', vertical_char=''):
    string = "<code>"
    for i in arr:
        for part in i:
            if isinstance(part, float) and round_numbers: part = round(part, round_numbers)
            part = str(part)
            if len(part) < target_length: part += horizontal_char * (target_length - len(part))
            string += part + vertical_char
        string += '\n'
    string += "</code>"
    return string

def get_weight(chances, text):
    return [[chances[i][1], text.count(chances[i][1]), chances[i][0], chances[i][0] * log2(chances[i][0]) * -1] for i in
            range(len(chances))]

def get_alphabet(text):
    return list(set(text))

def get_chances_count(text, alphabet):
    return [[text.count(alphabet[i]) / len(text), alphabet[i]] for i in range(len(alphabet))]