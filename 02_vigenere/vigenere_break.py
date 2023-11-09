import sys
import krypto_vigenere_main as vigenere_chiffre

V = vigenere_chiffre.Viginere()
if len(sys.argv) == 3:
    input_file = sys.argv[1]
    output_file = sys.argv[3]

    V.break_vigenere_file(input_file, output_file)
elif len(sys.argv) == 1:
    input_file = "sampleEncrypted.txt"
    output_file = "sampleDecrypted.txt"

    V.break_vigenere_file(input_file, output_file)
else:
    print("Wrong Number of Arguments. You have to give an input_file name as well as a output_file name.")