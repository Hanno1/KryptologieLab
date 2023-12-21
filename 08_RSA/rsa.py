import sys
import rsa_numbers as rn

if len(sys.argv) == 4:
    input_file = sys.argv[1]
    key_file = sys.argv[2]
    output_file = sys.argv[3]

    input = int(open(input_file, 'r').read().strip())
    key = [int(x) for x in open(key_file, 'r').read().strip().split('\n')]

    res = rn.rsa_alg(key, input)
    open(output_file, 'w').write(str(res))
else:   
    raise Exception("Wrong number of arguments! It has to be 3 but is " + str(len(sys.argv) - 1))