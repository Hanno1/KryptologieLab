import sys 
import helperclass as hc
import spn_main as spn

"""
main file to encrypt a text with the spn
"""

if len(sys.argv) == 4:
    inputfile = sys.argv[1]
    keyfile = sys.argv[2]
    outputfile = sys.argv[3]

    input =hc.bit_string_to_text(hc.hex_string_to_bit_string(hc.read_file(inputfile).replace(" ", "").replace("\n", "")))
    key = hc.read_file(keyfile).replace(" ", "").replace("\n", "")

    # encrypt the text with the random key
    spn = spn.SubstitutionPermutationNetwork(key)
    enc = spn.encrypt(input)

    hex_enc = hc.bit_string_to_hex_string(hc.text_to_bit_string(enc))
    hc.write_file(hc.hex_string_to_nice_hex_string(hex_enc), outputfile)
