ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Quelle: https://de.wikipedia.org/wiki/Buchstabenhäufigkeit
TRUE_VALUES = [0.0652, 0.0189, 0.0306, 0.0508, 0.1740, 0.0166, 0.0301, 0.0476, 0.0755, 0.0027, 0.0121, 0.0344, 0.0253, 0.0978, 0.0251, 0.0067, 0.0002, 0.0700, 0.0727, 0.0615, 0.0435, 0.0067, 0.0189, 0.0003, 0.0004, 0.0113]
M = len(ALPHABET)

def read_file(input_file):
    content = ""
    with open(input_file) as file:
        for line in file:
            content += line
    return content

def write_file(string, output_file):
    file = open(output_file, "w")
    file.write(string)
    file.close
    return 1

def char_to_number(char):
    return ord(char) - 65

def number_to_char(number):
    return chr(number + 65)

def get_text_length(content):
    length = 0
    for char in content:
        length += 1 if char in ALPHABET else 0
    return length
