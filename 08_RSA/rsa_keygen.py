import sys
import rsa_keygen_main

"""
main file to generate the rsa keys as in the slides
"""

if len(sys.argv) == 5:
    length = sys.argv[1]
    key_private = sys.argv[2]
    key_open = sys.argv[3]
    prime_numbers = sys.argv[4]

    e, d, p, q = rsa_keygen_main.generate_key(int(length))
    n = p * q
    open(key_private, 'w').write(str(d) + '\n' + str(n))
    open(key_open, 'w').write(str(e) + '\n' + str(n))
    open(prime_numbers, 'w').write(str(p) + '\n' + str(q))
else:   
    raise Exception("Wrong number of arguments! It has to be 4 but is " + str(len(sys.argv) - 1))