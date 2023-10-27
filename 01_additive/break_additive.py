import sys
import additive_chiffre

if len(sys.argv) == 3:
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    additive = additive_chiffre.AdditiveChiffre()
    additive.break_chiffre(input_file, output_file)
elif len(sys.argv) == 1:
    input_file = "sampleEncrypted.txt"
    output_file = "sampleDecrypted.txt"

    additive = additive_chiffre.AdditiveChiffre()
    additive.break_chiffre(input_file, output_file)
