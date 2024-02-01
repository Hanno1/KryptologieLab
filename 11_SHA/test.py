import sys
import helperclass as hc

r = 1152
c = 448
b = r + c
d = 224

BITS_64 = 0xffffffffffffffff

# Pad the input message (received as a bit string, return as a string)
pad = lambda N: N+'1'+'0'*(-(len(N) + 2) % r)+'1'
# Create blocks (received as a string, return as a list of integers) 
# (this pads the blocks as well)
blocks = lambda P: [int(P[i:i+r]+'0'*c, 2) for i in range(0, len(P), r)]
# Parity function on string table
par = lambda a, j, k: ''.join([a[i][j][k] for i in range(5)]).count('1') % 2
# XOR function on single character strings
xor = lambda *args: str(sum([int(a) for a in args]) % 2)

def f(b):
    # create a[i][j]
    # a[i][j] ist i-te Zeile, j-te Spalte (und 64 − k'tes Bit)
    a = [[0 for _ in range(5)] for _ in range(5)]
    b_temp = b
    for i in reversed(range(5)):
        for j in reversed(range(5)):
            a[i][j] = [*(bin(b_temp & BITS_64)[2:].zfill(64))][::-1]
            b_temp >>= 64
    # run 24 rounds of the algorithm
    for _ in range(24):
        a_temp = a.copy()
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    # a[i][j][k]    = a[i][j][k] xor par(a[0..4][j−1][k]) xor par(a[0..4][j+1][k−1])
                    a_temp[i][j][k] = xor(a[i][j][k], par(a, (j-1)%5, k), par(a, (j+1)%5, (k-1)%64))
    res = int(''.join([''.join([''.join(a[i][j]) for j in range(5)]) for i in range(5)]), 2)
    return res

# read input file as a string
input_file_path, output_file_path = sys.argv[1], sys.argv[2]
input_string = open(input_file_path, 'r').read().replace(" ", "")
# input_string = hc.text_to_bit_string(input_string)
# convert input string to bit string
input_bits = bin(int(input_string, 16))[2:].zfill(len(input_string) * 4)
# pad and create input blocks (as integers)
input_blocks = blocks(pad(input_bits))

# calculate the hash
s = 0
for i in range(len(input_blocks)):
    s = s ^ f(input_blocks[i])

# write first d//4 hex digits of the hash to the output file (padding with 0s if necessary)
# open(output_file_path, 'w').write(hex(s)[2:].zfill(b//4)[:d//4])
print(hex(s)[2:].zfill(b//4)[:d//4])
