import sys
import random
import spn_main as spn
import helperclass as hc

text_count = 8000
repetitions = 1

if len(sys.argv) > 1:
    text_count = int(sys.argv[1])
if len(sys.argv) > 2:
    repetitions = int(sys.argv[2])


for i in range(repetitions):
    random_key = ''.join([hex(random.randint(0, 15))[2:] for _ in range(4)])
    random_text = ''.join([hex(random.randint(0, 15))[2:] for _ in range(text_count * 4)])
    network = spn.SubstitutionPermutationNetwork(random_key)
    encrypted = hc.bit_string_to_hex_string(hc.text_to_bit_string(network.encrypt(random_text, enc_hex=True)))
    key = network.get_part_keys(random_text, encrypted)
    print(f'real key {random_key}, result key: {key}')
