import sys
import krypto_additive_main as additive_chiffre

if len(sys.argv) == 4:
    input_file = sys.argv[1]
    key = int(sys.argv[2])
    output_file = sys.argv[3]
    
    A = additive_chiffre.Additive_Chiffre(key = key)
    A.decrypt_file(input_file, output_file)
elif len(sys.argv) == 2:
    input_file = "encrypted.txt"
    key = int(sys.argv[1])
    output_file = "decrypted.txt"

    A = additive_chiffre.Additive_Chiffre(key = key)
    A.decrypt_file(input_file, output_file)
else:
    print("Wrong Number of Arguments. You have to give an input_file name, a key as well as a output_file name. If you only give a key we will use the std input file original.txt and std output file encrypted.txt!")