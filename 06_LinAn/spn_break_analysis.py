import sys
import random
import spn_main as spn
import helperclass as hc
import matplotlib.pyplot as plt

"""
main function to test the breaking of the spn - analysis. It generates random keys and texts and checks if a part key can be recovered
the dependencies of text_count and accuracy of the partkeys can be computed here
"""

def get_prob_correct(reps, tc):
    one_correct_keys = 0
    two_correct_keys = 0
    for i in range(reps):
        random_key = ''.join([hex(random.randint(0, 15))[2:] for _ in range(4)])
        random_text = ''.join([hex(random.randint(0, 15))[2:] for _ in range(tc * 4)])

        # encrypt the text with the random key
        network = spn.SubstitutionPermutationNetwork(random_key)
        encrypted = hc.bit_string_to_hex_string(hc.text_to_bit_string(network.encrypt(random_text, enc_hex=True)))
        
        # get the part key
        key = network.get_part_keys(random_text, encrypted)
        res_key = []
        res_key.append(hex(key[0])[2:])
        res_key.append(hex(key[1])[2:])
        if res_key[0] == random_key[1] and res_key[1] == random_key[3]:
            two_correct_keys += 1
        elif res_key[0] == random_key[1] or res_key[1] == random_key[3]:
            one_correct_keys += 1
        print(f'real key {random_key}, result key: *{res_key[0]}*{res_key[1]}')
    return two_correct_keys / reps, one_correct_keys / reps, (two_correct_keys + one_correct_keys) / reps

# textlength of random texts
text_count = 8000
# repeat for this many times
repetitions = 1

if len(sys.argv) > 1:
    text_count = int(sys.argv[1])
if len(sys.argv) > 2:
    repetitions = int(sys.argv[2])
get_prob_correct(repetitions, text_count)

# plot graph with probabilities depending on the text length
# x_values = [i for i in range(1_000, 12_000, 1_000)]
# repetitions = 10

# y_both = []
# y_least_one = []

# for x in x_values:
#     print("Starting with x = ", x)
#     print("---------------------")
#     p1, p2, p3 = get_prob_correct(repetitions, x)
#     y_both.append(p1)
#     y_least_one.append(p3)

# print(y_both)
# print(y_least_one)

# plt.figure(figsize=(8, 6))
# plt.plot(x_values, y_both, label="both keys correct")
# plt.plot(x_values, y_least_one, label="at least one key correct")
# plt.xlabel("textlength")
# plt.ylabel("probability")

# plt.legend()
# plt.show()

