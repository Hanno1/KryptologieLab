def read_file(input_file):
    """
    reads a file and returns the content as a string
    """
    content = ""
    with open(input_file) as file:
        for line in file:
            content += line
    return content

def write_file(string, output_file):
    """
    writes a string to a file
    """
    file = open(output_file, "w")
    file.write(string)
    file.close
    return 1

def xor_add(bit_string1, bit_string2):
    """
    xor adds two bit strings
    """
    bit_string = ""
    for i in range(len(bit_string1)):
        bit_string += str(int(bit_string1[i]) ^ int(bit_string2[i]))
    return bit_string

def int_to_byte(integer):
    # converts an integer to a bit string (1 byte)
    return bin(integer)[2:].zfill(8)

def int_to_bit_4(integer):
    # converts an integer to a bit string (4 bit)
    return bin(integer)[2:].zfill(4)

def char_to_byte(char):
    # converts a char to a bit string (1 byte)
    return bin(ord(char))[2:].zfill(8)

def bit_to_char(bit):
    # converts a bit string (1 byte) to a char
    return chr(int(bit, 2))

def text_to_bit_string(text):
    """
    converts an entire text to a bit string
    """
    bit_string = ""
    for char in text:
        bit_string += str(char_to_byte(char))
    return bit_string

def bit_string_to_text(bit_string):
    """
    converts a bit string back to a text
    """
    text = ""
    for i in range(0, len(bit_string), 8):
        text += bit_to_char(bit_string[i:i+8])
    return text

def bit_string_to_hex_string(bit_string):
    """
    converts a bit string to a hex string
    """
    hex_string = ""
    for i in range(0, len(bit_string), 4):
        hex_string += hex(int(bit_string[i:i+4], 2))[2:]
    return hex_string

def hex_string_to_bit_string(hex_string):
    """
    converts a hex string to a bit string
    """
    bit_string = ""
    for el in hex_string:
        try:
            bit_string += int_to_byte(int(el, 16))[4:]
        except:
            print("Error in hex_string_to_bit_string: " + el)
            raise ValueError
    return bit_string

def hex_string_to_nice_hex_string(hex_string):
    """
    adds spaces to a hex string to make it more readable
    """
    nice_hex_string = ""
    for i in range(0, len(hex_string), 2):
        nice_hex_string += hex_string[i:i+2] + " "
    return nice_hex_string


if __name__ == "__main__":
    print(bit_string_to_hex_string("0000000000011011"))
    print(hex_string_to_bit_string("001b2"))
