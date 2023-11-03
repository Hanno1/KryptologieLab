import sys
import krypto_02_vigenere as vigenere_chiffre

if len(sys.argv) == 3:
    input_file = sys.argv[1]
    output_file = sys.argv[3]

    vigenere_chiffre.break_vigenere_file(input_file, output_file)
elif len(sys.argv) == 1:
    input_file = "02_vigenere/sampleEncrypted.txt"
    output_file = "02_vigenere/sampleDecrypted.txt"

    vigenere_chiffre.break_vigenere_file(input_file, output_file)
else:
    print("Wrong Number of Arguments. You have to give an input_file name as well as a output_file name.")