import helperclass as hc

d = 224
r = 1152
c = 448
b = c + r

rotation = [[0, 1, 62, 28, 27],
            [36, 44, 6, 55, 20],
            [3, 10, 43, 25, 39],
            [41, 45, 15, 21, 8],
            [18, 2, 61, 56, 14]]

# round constants as hex strings
roundConstantsHex = [
    "0000000000000001",
    "0000000000008082",
    "800000000000808A",
    "8000000080008000",
    "000000000000808B",
    "0000000080000001",
    "8000000080008081",
    "8000000000008009",
    "000000000000008A",
    "0000000000000088",
    "0000000080008009",
    "000000008000000A",
    "000000008000808B",
    "800000000000008B",
    "8000000000008089",
    "8000000000008003",
    "8000000000008002",
    "8000000000000080",
    "000000000000800A",
    "800000008000000A",
    "8000000080008081",
    "8000000000008080",
    "0000000080000001",
    "8000000080008008"]

# convert to little endian
roundConstantsHex = [hc.hex_to_little_endian(hc.clean_hex(hex)) for hex in roundConstantsHex]
# convert to binary
roundConstantsBinary = [hc.hex_string_to_binary(hex) for hex in roundConstantsHex]

def get_coord(i,j,k):
    """
    calculate coordinate for string slicing -> modulo to wrap around
    """
    return (i % 5) * 320 + (j % 5) * 64 + (k % 64)

def get_block(block,i,j):
    """
    returns array of 64 bits from string block and coordinates i,j
    """
    return block[get_coord(i,j,0):get_coord(i,j,0)+64]

def get_parity(block,j,k):
    """
    returns the parity of the column j at position k
    """
    bs = [block[get_coord(i,j,k)] for i in range(5)]
    return hc.xor(bs[0],bs[1],bs[2],bs[3],bs[4])

def hash(block):
    """
    hash function -> 24 rounds of functions theta, rho, pi, chi, iota
    """
    for i in range(24):
        block = theta(block)
        block = rho(block)
        block = pi(block)
        block = chi(block)
        block = iota(block,i)
    return block

def theta(block):
    """
    implemented theta as in slides using string slicing
    """
    out = ""
    for i in range(5):
        for j in range(5):
            for k in range(64):
                out += hc.xor(block[get_coord(i,j,k)], get_parity(block,j-1,k), get_parity(block,j+1,k-1))
    return out

def rho(block):
    """
    implemented rho rotation as in slides
    """
    out = ""
    for i in range(5):
        for j in range(5):
            sub_block = get_block(block,i,j)
            # the current end of the block is the beginning of the new block
            out += sub_block[64-rotation[i][j]:] + sub_block[:64-rotation[i][j]]
    return out

def pi(block):
    """
    rotation as in slides
    """
    out = ""
    for i in range(5):
        for j in range(5):
            out += get_block(block,j,3*i+j)
    return out

def chi(block):
    """
    non linear function chi as in slides
    """
    out = ""
    for i in range(5):
        for j in range(5):
            out += hc.xor(get_block(block,i,j), hc.and_(hc.not_(get_block(block,i,j+1)), get_block(block,i,j+2)))
    return out

def iota(block,r):
    """
    add roundconstant to the first 64 bits of the block
    """
    return hc.xor(block[:64], roundConstantsBinary[r]) + block[64:]

def padding(msg):
    """
    add padding to the message as per sha3 224
    """
    msg = msg + "011"
    while (len(msg) + 1) % r != 0:
        msg = msg + "0"
    msg += "1"
    blocks = [msg[i:i+r] for i in range(0, len(msg), r)]
    return blocks

def main_alg(msg):
    """
    main algorithm of sha 3 224
    used to start the hash function
    """
    blocks = padding(msg)
    s = "0" * b
    for block in blocks:
        s = hash(hc.xor(s, block+("0"*c)))
    return s[:d]
