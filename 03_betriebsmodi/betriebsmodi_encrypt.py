import sys
import krypto_cbc_main as cbc
import krypto_ctr_main as ctr
import krypto_ecb_main as ecb
import krypto_ofb_main as ofb
from aes_keygen import aes_keygen
import helperclass as hc

"""
main function to encrypt with aes and a betriebsmodi
"""

def compute_betriebsmodi(betriebsmodus, input_file, key_file, output_file, iv="0"*128):
    """
    computes the aes encryption using the given betriebsmodus. 
    AES is for encrypting blocks and the betriebsmodi for encrypting the whole file and therefore defining the blocks used by the aes

    the key file is the file containing the key in hex -> a single key in this case since the remaining keys will be generated 
    by the aes_keygen function
    """
    betriebsmodi = None
    # get 11 keys
    key = hc.read_file(key_file).replace("\n", "").replace(" ", "")
    keys = aes_keygen(key)

    # get the betriebsmodi
    if iv != "0"*128:
        iv = hc.hex_string_to_bit_string(hc.read_file(iv).replace("\n", "").replace(" ", ""))
    if betriebsmodus.upper() == "ECB":
        betriebsmodi = ecb.ECB(key=keys)
    elif betriebsmodus.upper() == "CBC":
        betriebsmodi = cbc.CBC(initialisation=iv, key=keys)
    elif betriebsmodus.upper() == "OFB":
        betriebsmodi = ofb.OFB(initialisation=iv, key=keys)
    elif betriebsmodus.upper() == "CTR":
        betriebsmodi = ctr.CTR(key=keys)
    else:
        raise Exception("Wrong Betriebsmodus. Please choose ECB, CBC, CTR or OFB!")
    
    # translate the hex string to a bit string and apply the betriebsmodi
    text = hc.hex_string_to_bit_string(hc.read_file(input_file).replace(" ", ""))
    result = betriebsmodi.encrypt_text(hc.bit_string_to_text(text))

    # translate the bit string back to a hex string and write it to the output file
    hex_result = hc.bit_string_to_hex_string(hc.text_to_bit_string(result))
    act_hex_result = hc.hex_string_to_nice_hex_string(hex_result)

    hc.write_file(act_hex_result, output_file)

# input functionallity -> there can be an Inititalization file or not
if len(sys.argv) == 5:
    betriebsmodus = sys.argv[1]
    input_file = sys.argv[2]
    key_file = sys.argv[3]
    output_file = sys.argv[4]

    compute_betriebsmodi(betriebsmodus, input_file, key_file, output_file)
elif len(sys.argv) == 6:
    betriebsmodus = sys.argv[1]
    input_file = sys.argv[2]
    key_file = sys.argv[3]
    output_file = sys.argv[4]
    iv = sys.argv[5]

    compute_betriebsmodi(betriebsmodus, input_file, key_file, output_file, iv)
else:
    raise Exception("Wrong Number of Arguments. Please use: python3 betriebsmodi_encrypt.py <betriebsmodus> <input_file> <key_file> <output_file> [<iv>] there iv is optional")
    