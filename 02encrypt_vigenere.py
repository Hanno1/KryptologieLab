import sys
import krypto_02_vigenere as vigenere

if len(sys.argv) == 4:
    input_file = sys.argv[1]
    key = sys.argv[2]
    output_file = sys.argv[3]

    vigenere.encrypt_file(input_file, output_file, key)
elif len(sys.argv) == 2:
    input_file = "02_vigenere/original.txt"
    key = sys.argv[1]
    output_file = "02_vigenere/encrypted.txt"

    vigenere.encrypt_file(input_file, output_file, key)
else:
    print("Wrong Number of Arguments!")