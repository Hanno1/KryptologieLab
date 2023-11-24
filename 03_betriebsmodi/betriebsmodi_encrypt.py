import sys
import krypto_cbc_main as cbc
import krypto_ctr_main as ctr
import krypto_ecb_main as ecb
import krypto_ofb_main as ofb
from aes_keygen import aes_keygen
import helperclass as hc


def compute_betriebsmodi(betriebsmodus, input_file, key_file, output_file, iv="0"*128):
    betriebsmodi = None
    key = hc.read_file(key_file).replace("\n", "").replace(" ", "")
    keys = aes_keygen(key)
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
    text = hc.hex_string_to_bit_string(hc.read_file(input_file).replace(" ", ""))
    result = betriebsmodi.encrypt_text(hc.bit_string_to_text(text))

    hex_result = hc.bit_string_to_hex_string(hc.text_to_bit_string(result))
    act_hex_result = hc.hex_string_to_nice_hex_string(hex_result)

    hc.write_file(act_hex_result, output_file)

if len(sys.argv) == 5:
    betriebsmodus = sys.argv[1]
    input_file = sys.argv[2]
    key_file = sys.argv[3]
    output_file = sys.argv[4]

    text = hc.read_file(input_file)
    bit_text = hc.text_to_bit_string(text)
    hex_text = hc.bit_string_to_hex_string(bit_text)
    nice_hex_text = hc.hex_string_to_nice_hex_string(hex_text)

    hc.write_file(nice_hex_text, output_file)

    # compute_betriebsmodi(betriebsmodus, input_file, key_file, output_file)
elif len(sys.argv) == 6:
    betriebsmodus = sys.argv[1]
    input_file = sys.argv[2]
    key_file = sys.argv[3]
    output_file = sys.argv[4]
    iv = sys.argv[5]

    compute_betriebsmodi(betriebsmodus, input_file, key_file, output_file, iv)
else:
    raise Exception("Wrong Number of Arguments. You have to give an input_file name, a key as well as a output_file name. If you only give a key we will use the std input file original.txt and std output file encrypted.txt!")
    