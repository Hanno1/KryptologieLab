SBOX = [99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118, 202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164, 114, 192, 183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49, 21, 4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117, 9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47, 132, 83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207, 208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168, 81, 163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210, 205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 115, 96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219, 224, 50, 58, 10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121, 231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174, 8, 186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138, 112, 62, 181, 102, 72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158, 225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206, 85, 40, 223, 140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22]

SBOX_INV = [82, 9, 106, 213, 48, 54, 165, 56, 191, 64, 163, 158, 129, 243, 215, 251, 124, 227, 57, 130, 155, 47, 255, 135, 52, 142, 67, 68, 196, 222, 233, 203, 84, 123, 148, 50, 166, 194, 35, 61, 238, 76, 149, 11, 66, 250, 195, 78, 8, 46, 161, 102, 40, 217, 36, 178, 118, 91, 162, 73, 109, 139, 209, 37, 114, 248, 246, 100, 134, 104, 152, 22, 212, 164, 92, 204, 93, 101, 182, 146, 108, 112, 72, 80, 253, 237, 185, 218, 94, 21, 70, 87, 167, 141, 157, 132, 144, 216, 171, 0, 140, 188, 211, 10, 247, 228, 88, 5, 184, 179, 69, 6, 208, 44, 30, 143, 202, 63, 15, 2, 193, 175, 189, 3, 1, 19, 138, 107, 58, 145, 17, 65, 79, 103, 220, 234, 151, 242, 207, 206, 240, 180, 230, 115, 150, 172, 116, 34, 231, 173, 53, 133, 226, 249, 55, 232, 28, 117, 223, 110, 71, 241, 26, 113, 29, 41, 197, 137, 111, 183, 98, 14, 170, 24, 190, 27, 252, 86, 62, 75, 198, 210, 121, 32, 154, 219, 192, 254, 120, 205, 90, 244, 31, 221, 168, 51, 136, 7, 199, 49, 177, 18, 16, 89, 39, 128, 236, 95, 96, 81, 127, 169, 25, 181, 74, 13, 45, 229, 122, 159, 147, 201, 156, 239, 160, 224, 59, 77, 174, 42, 245, 176, 200, 235, 187, 60, 131, 83, 153, 97, 23, 43, 4, 126, 186, 119, 214, 38, 225, 105, 20, 99, 85, 33, 12, 125]

RCON = [1, 2, 4, 8, 16, 32, 64, 128, 27, 54]

MIX_COL = [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]]

MIX_COL_INV = [[14, 11, 13, 9], [9, 14, 11, 13], [13, 9, 14, 11], [11, 13, 9, 14]]

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

def check_aes_key(keys, block_length):
    if len(keys) != 11:
        raise Exception("Wrong number of keys! It has to be 11 but is " + str(len(keys)))
    for index, key in enumerate(keys):
        if len(key) != block_length:
            raise Exception("Wrong length of key " + str(index) + "! It has to be " + str(block_length) + " but is " + str(len(key)))

def xor_add(bit_string1, bit_string2):
    bit_string = ""
    for i in range(len(bit_string1)):
        bit_string += str(int(bit_string1[i]) ^ int(bit_string2[i]))
    return bit_string

def int_to_bit(integer):
    return bin(integer)[2:].zfill(8)

def int_to_bit_4(integer):
    return bin(integer)[2:].zfill(4)

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

def bit_string_to_hex_string(bit_string):
    hex_string = ""
    for i in range(0, len(bit_string), 4):
        hex_string += hex(int(bit_string[i:i+4], 2))[2:]
    return hex_string

def hex_string_to_bit_string(hex_string):
    bit_string = ""
    for el in hex_string:
        bit_string += int_to_bit(int(el, 16))[4:]
    return bit_string

def read_key_from_file(file_name):
    keys = []
    with open(file_name) as f:
        for line in f:
            line = line.replace(" ", "").replace("\n", "")
            keys.append(hex_string_to_bit_string(line))
    return keys

def hex_string_to_nice_hex_string(hex_string):
    nice_hex_string = ""
    for i in range(0, len(hex_string), 2):
        nice_hex_string += hex_string[i:i+2] + " "
    return nice_hex_string


if __name__ == "__main__":
    print(bit_string_to_hex_string("0000000000011011"))
    print(hex_string_to_bit_string("001b2"))
