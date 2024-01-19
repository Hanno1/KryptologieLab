import sys
import krypto_vigenere_main as vigenere

"""
main function to encrypt using the vigenere chiffre
"""

if len(sys.argv) == 4:
    input_file = sys.argv[1]
    key = sys.argv[2]
    output_file = sys.argv[3]

    V = vigenere.Viginere(key)
    V.encrypt_file(input_file, output_file)

else:
    print("Wrong Number of Arguments! Has to be 3: input_file, key, output_file")