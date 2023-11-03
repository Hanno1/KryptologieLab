import sys
import krypto_01_additive as additive_chiffre

if len(sys.argv) == 3:
    input_file = sys.argv[1]
    output_file = sys.argv[3]

    additive_chiffre.break_additive_file(input_file, output_file)
elif len(sys.argv) == 1:
    input_file = "01_additive/sampleEncrypted.txt"
    output_file = "01_additive/sampleDecrypted.txt"

    additive_chiffre.break_additive_file(input_file, output_file)
else:
    print("Wrong Number of Arguments. You have to give an input_file name as well as a output_file name.")