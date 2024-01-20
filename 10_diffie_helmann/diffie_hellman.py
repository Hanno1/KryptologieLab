import sys
import diffie_hellman_keyexchange

"""
main file to start the diffie hellman key exchange as in the slides
"""

if len(sys.argv) == 2:
    bits = sys.argv[1]
    s1, s2 = 1, 0
    p, g, a, b = 0, 0, 0, 0
    while s1 != s2:
        s1, s2, p, g, a, b = diffie_hellman_keyexchange.get_result(int(bits))
        if s1 != s2:
            print("Secret difference between A and B: ", s1, " ", s2, " ?!? :(")
    print("prime p: ", p)
    print("generator g: ", g)
    print("Alice's computation A: ", a)
    print("Bob's computation B: ", b)
    print("secret S: ", s1)
else:   
    raise Exception("Wrong number of arguments! It has to be 4 but is " + str(len(sys.argv) - 1))