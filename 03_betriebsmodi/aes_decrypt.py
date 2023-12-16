import sys
import aes as aes
import helperclass as hc

if len(sys.argv) == 4:
    input_file = sys.argv[1]
    key_file = sys.argv[2]
    output_file = sys.argv[3]

    keys = hc.read_key_from_file(key_file)
    with open(input_file) as f:
        content = f.read().replace("\n", "").replace(" ", "")
    bit_string = hc.hex_string_to_bit_string(content)

    alg = aes.AES()
    dec = hc.bit_string_to_hex_string(alg.decrypt(bit_string, keys))
    new_dec = ''
    for i in range(0, len(dec), 2):
        new_dec += dec[i: i + 2] + ' '
    with open(output_file, "w") as f:
        f.write(new_dec)