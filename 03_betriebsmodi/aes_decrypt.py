import sys
import aes as aes
import helperclass as hc

"""
main function to decrypt blocks with aes
"""

if len(sys.argv) == 4:
    input_file = sys.argv[1]
    key_file = sys.argv[2]
    output_file = sys.argv[3]

    # get all 11 keys
    keys = hc.read_key_from_file(key_file)

    # get text to decrypt
    with open(input_file) as f:
        content = f.read().replace("\n", "").replace(" ", "")
    bit_string = hc.hex_string_to_bit_string(content)

    # actual decryption
    alg = aes.AES()
    dec = hc.bit_string_to_hex_string(alg.decrypt(bit_string, keys))
    # convert it to nicer format with spaces between every two chars
    new_dec = hc.hex_string_to_nice_hex_string(dec)

    with open(output_file, "w") as f:
        f.write(new_dec)