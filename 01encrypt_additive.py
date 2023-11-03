import sys
import krypto_01_additive as additive_chiffre

if len(sys.argv) == 4:
    input_file = sys.argv[1]
    key = int(sys.argv[2])
    output_file = sys.argv[3]

    additive_chiffre.encrypt_file(input_file, key, output_file)
elif len(sys.argv) == 2:
    input_file = "01_additive/original.txt"
    key = int(sys.argv[1])
    output_file = "01_additive/encrypted.txt"

    additive_chiffre.encrypt_file(input_file, key, output_file)
else:
    print("Wrong Number of Arguments. You have to give an input_file name, a key as well as a output_file name. If you only give a key we will use the std input file original.txt and std output file encrypted.txt!")