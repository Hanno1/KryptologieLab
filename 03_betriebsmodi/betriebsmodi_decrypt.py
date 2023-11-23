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
    text = hc.hex_string_to_bit_string(hc.read_file(input_file).replace("\n", "").replace(" ", ""))
    result = betriebsmodi.decrypt_text(hc.bit_string_to_text(text))

    print("Result: ", result)

    hex_result = hc.bit_string_to_hex_string(hc.text_to_bit_string(result))
    act_hex_result = ""
    for i in range(0, len(hex_result), 2):
        act_hex_result += hex_result[i:i+2] + " "

    print("write File " + act_hex_result)

    hc.write_file(act_hex_result, output_file)

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
    raise Exception("Wrong Number of Arguments. You have to give an input_file name, a key as well as a output_file name. If you only give a key we will use the std input file original.txt and std output file encrypted.txt!")
    