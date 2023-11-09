import sys
import krypto_vigenere_main as vigenere

if len(sys.argv) == 4:
    input_file = sys.argv[1]
    key = sys.argv[2]
    output_file = sys.argv[3]

    V = vigenere.Viginere(key)
    V.decrypt_file(input_file, output_file)
elif len(sys.argv) == 2:
    input_file = "encrypted.txt"
    key = sys.argv[1]
    output_file = "decrypted.txt"

    V = vigenere.Viginere(key)
    V.decrypt_file(input_file, output_file)
else:
    print("Wrong Number of Arguments. You have to give an input_file name, a key as well as a output_file name. If you only give a key we will use the std input file original.txt and std output file encrypted.txt!")