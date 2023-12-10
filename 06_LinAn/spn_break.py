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
    with open('save_text.txt') as f:
        random_text = f.read()
    random_key = "a88b"
    # print("Run{:6d} of{:6d}:".format(i+1, repetitions))

    # random_text = "".join([hex(random.randint(0, 15))[2:] for _ in range(text_count * 4)])
    # random_key = "".join([hex(random.randint(0, 15))[2:] for _ in range(4)])

    network = spn.SubstitutionPermutationNetwork(random_key)
    encrypted = hc.bit_string_to_hex_string(hc.text_to_bit_string(network.encrypt(random_text, enc_hex=True)))
    key = network.get_part_keys(random_text, encrypted)

    # with open('save_enc.txt', 'w') as f:
    #     f.write(encrypted)

    # print(random_text)
    # print(random_key)

    # with open('save_text.txt', 'w') as f:
    #     f.write(random_text)

    print(f'real key: {random_key}, result key: *{key[0]}*{key[1]}')
