import helperclass as hc
import copy

ROTATIONS = [
    [0, 1, 62, 28, 27],
    [36, 44, 6, 55, 20],
    [3, 10, 43, 25, 39],
    [41, 45, 15, 21, 8],
    [18, 2, 61, 56, 14],
]

ROUND_CONSTANTS = [
    "0000000000000001",
    "0000000000008082",
    "800000000000808a",
    "8000000080008000",
    "000000000000808b",
    "0000000080000001",
    "8000000080008081",
    "8000000000008009",
    "000000000000008a",
    "0000000000000088",
    "0000000080008009",
    "000000008000000a",
    "000000008000808b",
    "800000000000008b",
    "8000000000008089",
    "8000000000008003",
    "8000000000008002",
    "8000000000000080",
    "000000000000800a",
    "800000008000000a",
    "8000000080008081",
    "8000000000008080",
    "0000000080000001",
    "8000000080008008"
]

r = 1152
c = 448
b = r + c
d = 224

def get_coord(i, j, k):
    return i * 320 + j * 64 + k

def main_hashing(message):
    message = padding(message)
    s = "0" * b
    for block in message:
        added = hc.xor_add(s, block + "0" * c)
        s = hash(added)
    s = hc.bit_string_to_hex_string(s)
    return s[:224//4]

def changeOrder(block):
    newBlock = ""
    for i in range(0, len(block), 8):
        newBlock += block[i:i+8][::-1]
    return newBlock

def padding(message):
    message += "011"
    while (len(message) + 1) % r != 0:
        message += "0"
    message += "1"
    # return k blocks of r bits
    return [changeOrder(message[i:i+r]) for i in range(0, len(message), r)]

def hash(value):
    # turn value into blocks of 64 bits
    value = [[value[i*320 + j*64:i*320 + j *64 + 64] for j in range(5)] for i in range(5)]
    for i in range(24):
        value = theta(value)
        value = rho(value)
        value = pi(value)
        value = chi(value)
        value = iota(value, i)
    # convert it back
    v = ""
    for i in range(5):
        for j in range(5):
            v += value[i][j]
    return v

def theta(value):
    current_value = []
    for i in range(0, 5):
        current_line = []
        for j in range(0, 5):
            v = ""
            for k in range(64):
                tmp = value[i][j][k]
                a1 = parity(value, (j - 1) % 5, k)
                a2 = parity(value, (j + 1) % 5, (k - 1) % 64)
                new_value = hc.xor_add(a1, hc.xor_add(a2, tmp))
                v += new_value
            current_line.append(v)
        current_value.append(current_line)
    return current_value

def parity(value, j, k):
    v = 0
    for i in range(0, 4):
        v += int(value[i][j][k], 2)
    return str(v % 2)

def rho(value):
    new_value = []
    for i in range(0, 5):
        new_line = []
        for j in range(0, 5):
            line = value[i][j]
            current_rotation_value = ROTATIONS[i][j]
            new_line.append(rotateBitString(line, current_rotation_value))
        new_value.append(new_line)
    return new_value

def rotateBitString(value, n):
    return value[n:] + value[:n]

def pi(value):
    current_value = []
    for i in range(5):
        current_line = []
        for j in range(5):
            current_line.append(value[j][(3 * i + j) % 5])
        current_value.append(current_line)        
    return current_value

def chi(value):
    current_value = []
    for i in range(5):
        current_line = []
        for j in range(5):
            result = hc.xor_add(value[i][j], hc.and_bits(value[i][(j+1)%5], hc.negate(value[i][(j+2) % 5])))
            current_line.append(result)
        current_value.append(current_line)
    return value

def iota(value, c):
    value[0][0] = hc.xor_add(value[0][0], hc.hex_string_to_bit_string(ROUND_CONSTANTS[c]))
    return value





# def convert_to_blocks(block):
#     lines = [block[i*320:i*320 + 320] for i in range(5)]
#     new_lines = []
#     for line in lines:
#         # new_lines.append([line[i*64:i*64 + 64] for i in range(5)])
#         new_lines.append([[line[i*64:i*64 + 64][j] for j in range(64)] for i in range(5)])
#     return new_lines

# def hash_mat(mat):
#     for _ in range(24):
#         current_mat = copy.deepcopy(mat)
#         for row in range(0, 5):
#             for col in range(0, 5):
#                 for k in range(64):
#                     tmp = mat[row][col][63 - k]
#                     a1 = parity_mat(mat, (col - 1) % 5, (63 - k))
#                     a2 = parity_mat(mat, (col + 1) % 5, (63 - ((k - 1) % 64)))
#                     new_value = hc.xor_add(a1, hc.xor_add(a2, tmp))
#                     current_mat[row][col][k] = new_value
#         mat = current_mat
#     return mat

# def parity_mat(mat, col, k):
#     v = 0
#     for row in range(0, 5):
#         v += int(mat[row][col][k], 2)
#     return str(1 - v % 2)

if __name__ == "__main__":
    # https://en.wikipedia.org/wiki/SHA-3
    # message = "Hallo Welt das ist ein lange Nachricht die gehasht werden soll. Ich hoffe das funktioniert. Ich bin mir aber nicht sicher. Der text ist aber noch nicht lange genug!"
    # message = hc.text_to_bit_string(message)

    message = open("test.txt").readlines()[0].replace(" ", "")
    print(message)
    message = hc.hex_string_to_bit_string(message)
    print(main_hashing(message))