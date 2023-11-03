import sys
import krypto_02_vigenere as vigenere

if len(sys.argv) == 4:
    input_file = sys.argv[1]
    key = sys.argv[2]
    output_file = sys.argv[3]

    vigenere.decrypt_file(input_file, output_file, key)
elif len(sys.argv) == 2:
    input_file = "02_vigenere/encrypted.txt"
    key = sys.argv[1]
    output_file = "02_vigenere/decrypted.txt"

    vigenere.decrypt_file(input_file, output_file, key)
else:
    print("Wrong Number of Arguments. You have to give an input_file name, a key as well as a output_file name. If you only give a key we will use the std input file original.txt and std output file encrypted.txt!")