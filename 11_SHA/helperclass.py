def char_to_bit(char):
    # character to byte
    return bin(ord(char))[2:].zfill(8)

def byte_to_char(bit):
    # byte to character
    return chr(int(bit, 2))

def int_to_byte(integer):
    # integer to byte
    return bin(integer)[2:].zfill(8)

def text_to_bit_string(text):
    """
    converts a text into a bit string -> encodes every char as byte
    """
    bit_string = ""
    for char in text:
        bit_string += str(char_to_bit(char))
    return bit_string

def bit_string_to_text(bit_string):
    """
    converts a bit string back into normal text
    """
    text = ""
    for i in range(0, len(bit_string), 8):
        text += byte_to_char(bit_string[i:i+8])
    return text

def xor_add(bit_string1, bit_string2):
    """
    takes 2 bitstrings and applies the XOR function to them. 
    It is implemented using strings because it is easier to understand.
    """
    bit_string = ""
    for i in range(len(bit_string1)):
        bit_string += str(int(bit_string1[i]) ^ int(bit_string2[i]))
    return bit_string

def negate(bit_string):
    """
    negates a bit string
    """
    new_bit_string = ""
    for char in bit_string:
        if char == "0":
            new_bit_string += "1"
        else:
            new_bit_string += "0"
    return bit_string

def and_bits(bit_string1, bit_string2):
    """
    takes 2 bitstrings and applies the AND function to them. 
    It is implemented using strings because it is easier to understand.
    """
    bit_string = ""
    for i in range(len(bit_string1)):
        c1 = bit_string1[i]
        c2 = bit_string2[i]
        if c1 == "1" and c2 == "1" or c1 == "0" and c2 == "0":
            bit_string += "0"
        else:
            bit_string += "1"
        bit_string += str(int(bit_string1[i]) & int(bit_string2[i]))
    return bit_string

def bit_string_to_hex_string(bit_string):
    """
    converts a bit string into a hex string -> take every 4 bits and convert them to one hex char
    """
    hex_string = ""
    for i in range(0, len(bit_string), 4):
        hex_string += hex(int(bit_string[i:i+4], 2))[2:]
    return hex_string

def hex_string_to_bit_string(hex_string):
    """
    converts a hex string into a bitstring
    """
    bit_string = ""
    for el in hex_string:
        bit_string += int_to_byte(int(el, 16))[4:]
    return bit_string
