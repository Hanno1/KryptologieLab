import sys
import sha_main
import helperclass as hc

# main
if len(sys.argv) != 3:
    print("Usage: python sha3.py input_file output_file")
    sys.exit(1)
    
input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r") as file:
    data = hc.hex_string_to_binary(file.read())

with open(output_file, "w") as file:
    file.write(hc.binary_string_to_hex(sha_main.main_alg(data)))