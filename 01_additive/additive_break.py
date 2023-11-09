import sys
import krypto_additive_main as additive_chiffre

A = additive_chiffre.Additive_Chiffre()
if len(sys.argv) == 3:
    input_file = sys.argv[1]
    output_file = sys.argv[3]

    A.break_additive_file(input_file, output_file)
elif len(sys.argv) == 1:
    input_file = "sampleEncrypted.txt"
    output_file = "sampleDecrypted.txt"

    A.break_additive_file(input_file, output_file)
else:
    print("Wrong Number of Arguments. You have to give an input_file name as well as a output_file name.")