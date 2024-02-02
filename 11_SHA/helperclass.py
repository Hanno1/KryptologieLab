def cleanHex(hex):
    """
    remove all non-hex characters from a hex string
    """
    return hex.replace(" ", "")

def hex_to_byte(hex):
    """
    converts 2 hex to 8 bit binary -> little endian
    """
    return bin(int(hex, 16))[2:].zfill(8)[::-1]

def hex_string_to_binary(hex):
    """
    convert an entire hex string into a binary string -> little endian
    """
    hex = cleanHex(hex)
    return "".join([hex_to_byte(hex[i:i+2]) for i in range(0, len(hex), 2)])

def byte_to_hex(binary):
    """
    converts a byte to 2 hex chars -> byte is in little endian
    """
    return hex(int(binary[::-1], 2))[2:].zfill(2)

def binary_string_to_hex(binary):
    return "".join([byte_to_hex(binary[i:i+8]) for i in range(0, len(binary), 8)])

def xor(*args):
    """
    bitwise xor on binary strings
    """
    return ''.join(str(sum(int(i) for i in x) % 2) for x in zip(*args))

def and_(*args):
    """
    bitwise and on binary strings
    """
    return ''.join(str(min(int(i) for i in x)) for x in zip(*args))

def not_(a):
    """
    bitwise not on binary string
    """
    new = ""
    for char in a:
        if char == "0":
            new += "1"
        else:
            new += "0"
    return new