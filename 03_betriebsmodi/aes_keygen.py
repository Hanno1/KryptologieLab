import helperclass as hc

def aes_keygen(key_hex_string):
    """
    keygeneration of the aes algorithm. It takes a hex string as input and returns a list of 11 keys
    its implemented using the algorithms from the slides

    the returned keys are in bit format
    """
    # translate the hex key to a bit format -> a key with 32 hexchars has 128 bits
    key_bit_string = hc.hex_string_to_bit_string(key_hex_string)
    ws = []
    for i in range(44):
        if i < 4:
            current_bit_string = key_bit_string[i * 32: i * 32 + 32]
            ws.append(current_bit_string)
        elif i % 4 == 0:
            new_bit_string = add_rcon(ws[i-4], i)
            ws.append(hc.xor_add(new_bit_string, sub_word(rot_words(ws[i-1]))))
        else:
            ws.append(hc.xor_add(ws[i-4], ws[i-1]))
    
    # join the keys back together -> take 4 words and join them to a key
    keys = []
    for j in range(0, 41, 4):
        current_key = ""
        for i in range(4):
            current_key += ws[j + i]
        keys.append(current_key)

    return keys

def add_rcon(bit_string, index):
    """
    rcon for a specific index. lookup in the RCON table
    """
    rcon = hc.RCON[(index // 4) - 1]
    rcon_value = bin(rcon)[2:].zfill(8) + "0" * 24
    return hc.xor_add(bit_string, rcon_value)

def rot_words(bit_string):
    """
    rotate the first byte to the right
    """
    pre = bit_string[:8]
    return bit_string[8:] + pre

def sub_word(bit_string):
    """
    apply a SBOX to the bit string
    """
    new_bit_string = ""
    for i in range(0, len(bit_string), 8):
        new_bit_string += hc.int_to_byte(hc.SBOX[int(bit_string[i:i+8], 2)])
    return new_bit_string


if __name__ == "__main__":
    key_hex_string = "2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c"
    key_hex_string = key_hex_string.replace(" ", "")
    keys = aes_keygen(key_hex_string)
    for key in keys:
        print(hc.bit_string_to_hex_string(key))
