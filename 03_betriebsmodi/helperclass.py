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

def char_to_bit(char):
    return bin(ord(char))[2:].zfill(8)

def char_to_string_bit(char):
    return str(char_to_bit(char))

def bit_to_char(bit):
    return chr(int(bit, 2))

def bit_string_to_char(bit_string):
    char_string = ""
    for i in range(0, len(bit_string), 8):
        char_string += bit_to_char(bit_string[i:i+8])
    return char_string

def text_to_bit_string(text):
    bit_string = ""
    for char in text:
        bit_string += char_to_string_bit(char)
    return bit_string

def bit_string_to_text(bit_string):
    text = ""
    for i in range(0, len(bit_string), 8):
        text += bit_to_char(bit_string[i:i+8])
    return text
