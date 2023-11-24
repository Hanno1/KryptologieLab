def char_to_bit(char):
    return bin(ord(char))[2:].zfill(8)

def bit_to_char(bit):
    return chr(int(bit, 2))

def text_to_bit_string(text):
    bit_string = ""
    for char in text:
        bit_string += str(char_to_bit(char))
    return bit_string

def bit_string_to_text(bit_string):
    text = ""
    for i in range(0, len(bit_string), 8):
        text += bit_to_char(bit_string[i:i+8])
    return text

res = text_to_bit_string(" (griechisch κρυπτός kryptós „versteckt, ")
print(res)

print(bit_string_to_text(res))
