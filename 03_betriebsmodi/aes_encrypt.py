import sys
import aes as aes
import helperclass as hc

"""
main function to encrypt block with aes
"""

if len(sys.argv) == 4:
    input_file = sys.argv[1]
    key_file = sys.argv[2]
    output_file = sys.argv[3]

    # get all 11 keys from this file
    keys = hc.read_key_from_file(key_file)
    # get text
    with open(input_file) as f:
        content = f.read().replace("\n", "").replace(" ", "")
    bit_string = hc.hex_string_to_bit_string(content)

    # actual encryption
    alg = aes.AES()
    enc = hc.bit_string_to_hex_string(alg.encrypt(bit_string, keys))
    # convert the hex string to a better format
    new_enc = hc.hex_string_to_nice_hex_string(enc)

    with open(output_file, "w") as f:
        f.write(new_enc)