import sys
import additive_chiffre

if len(sys.argv) == 4:
    input_file = sys.argv[1]
    key = int(sys.argv[2])
    output_file = sys.argv[3]

    additive = additive_chiffre.AdditiveChiffre(key)
    additive.decrypt(input_file, output_file)
elif len(sys.argv) == 2:
    input_file = "encrypted.txt"
    key = int(sys.argv[1])
    output_file = "decrypted.txt"

    additive = additive_chiffre.AdditiveChiffre(key)
    additive.decrypt(input_file, output_file)
else:
    print("Wrong Number of Arguments. You have to give an input_file name, a key as well as a output_file name. If you only give a key we will use the std input file original.txt and std output file encrypted.txt!")