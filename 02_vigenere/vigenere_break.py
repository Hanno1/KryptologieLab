import sys
import krypto_vigenere_main as vigenere_chiffre

"""
main function to break the vigenere chiffre
"""

V = vigenere_chiffre.Viginere()
if len(sys.argv) == 3:
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    V.break_vigenere_file(input_file, output_file)

else:
    print("Wrong Number of Arguments. You have to give an input_file name as well as a output_file name.")