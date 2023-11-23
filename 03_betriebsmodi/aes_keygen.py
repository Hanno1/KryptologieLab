import helperclass as hc

def aes_keygen(key_hex_string):
    key_bit_string = hc.hex_string_to_bit_string(key_hex_string)
    ws = []
    for i in range(44):
        current_bit_string = key_bit_string[i * 32: i * 32 + 32]
        if i < 4:
            ws.append(current_bit_string)
        elif i % 4 == 0:
            new_bit_string = add_rcon(ws[i-4], i)
            ws.append(hc.xor_add(new_bit_string, sub_word(rot_words(ws[i-1]))))
        else:
            ws.append(hc.xor_add(ws[i-4], ws[i-1]))
    
    keys = []
    for j in range(0, 41, 4):
        current_key = ""
        for i in range(4):
            current_key += ws[j + i]
        keys.append(current_key)

    return keys

def add_rcon(bit_string, index):
    rcon = hc.RCON[(index // 4) - 1]
    rcon_value = bin(rcon)[2:].zfill(8) + "0" * 24
    return hc.xor_add(bit_string, rcon_value)

def rot_words(bit_string):
    pre = bit_string[:8]
    return bit_string[8:] + pre

def sub_word(bit_string):
    new_bit_string = ""
    for i in range(0, len(bit_string), 8):
        new_bit_string += hc.int_to_bit(hc.SBOX[int(bit_string[i:i+8], 2)])
    return new_bit_string


if __name__ == "__main__":
    key_hex_string = "2b7e151628aed2a6abf7158809cf4f3c"
    keys = aes_keygen(key_hex_string)
    for key in keys:
        print(hc.bit_string_to_hex_string(key))
