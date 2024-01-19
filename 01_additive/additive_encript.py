import sys
import krypto_additive_main as additive_chiffre

"""
main program to decrypt the additive chiffre
"""

if len(sys.argv) == 4:
    input_file = sys.argv[1]
    key = int(sys.argv[2])
    output_file = sys.argv[3]

    A = additive_chiffre.Additive_Chiffre(key = key)
    A.encrypt_file(input_file, output_file)
else:
    print("Wrong Number of Arguments. You have to give an input_file name, a key as well as a output_file name.")