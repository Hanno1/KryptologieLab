import sys
import krypto_vigenere_main as vigenere

if len(sys.argv) == 4:
    input_file = sys.argv[1]
    key = sys.argv[2]
    output_file = sys.argv[3]

    V = vigenere.Viginere(key)
    V.encrypt_file(input_file, output_file)
elif len(sys.argv) == 2:
    input_file = "original.txt"
    key = sys.argv[1]
    output_file = "encrypted.txt"

    V = vigenere.Viginere(key)
    V.encrypt_file(input_file, output_file)
else:
    print("Wrong Number of Arguments!")