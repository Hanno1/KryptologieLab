import sys
import krypto_vigenere_main as vigenere

"""
main function to decrypt using the vigenere chiffre
"""

if len(sys.argv) == 4:
    input_file = sys.argv[1]
    key = sys.argv[2]
    output_file = sys.argv[3]

    V = vigenere.Viginere(key)
    V.decrypt_file(input_file, output_file)

else:
    print("Wrong Number of Arguments. You have to give an input_file name, a key as well as a output_file name.")