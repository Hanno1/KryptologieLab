import helperclass as hc

# SBOX used for this spn
S_BOX = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]
# permutation used for this spn
PERMUTATION = [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]

class SubstitutionPermutationNetwork:
    """
    class to encrypt or break a spn using the algorithm from the slides
    """
    def __init__(self, key) -> None:
        self.block_length = 16
        self.rounds = 4
        key = hc.hex_string_to_bit_string(key)
        self.keys = [key for _ in range(self.rounds + 1)]

    def get_blocks_of_bit_string(self, bit_string):
        # split the bit string into blocks of 16 bits
        return [bit_string[i:i+self.block_length] for i in range(0, len(bit_string), self.block_length)]

    def add_key(self, bit_string, round):
        # xor the bit string with the key
        return hc.xor_add(bit_string, self.keys[round])
    
    def substitution(self, bit_string):
        """
        apply the substitution box to the bit string and returns the substituted bit string
        """
        new_bit_string = ""
        for i in range(0, len(bit_string), 4):
            new_bit_string += hc.int_to_bit_4(S_BOX[int(bit_string[i:i+4], 2)])
        return new_bit_string
    
    def permutation(self, bit_string):
        """
        apply the permutation to the bit string and returns the permuted bit string
        """
        new_bits = [0 for _ in range(len(bit_string))]
        for i in range(0, len(bit_string)):
            new_bits[PERMUTATION[i] - 1] = bit_string[i]
        return ''.join(new_bits)

    def encrypt(self, plaintext, enc_hex=False):
        """
        encrypts the plaintext using the spn algorithm and returns the encrypted text
        """
        if enc_hex:
            bit_content = hc.hex_string_to_bit_string(plaintext)
        else:
            bit_content = hc.text_to_bit_string(plaintext)

        # divide the bit string into blocks of 16 bits and add padding if necessary
        bit_blocks = self.get_blocks_of_bit_string(bit_content)
        while len(bit_blocks[-1]) < self.block_length:
            bit_blocks[-1] += "0"
        encryption = ""

        # spn algorithm from the slides
        for bit_string in bit_blocks:
            for i in range(self.rounds - 1):
                bit_string = self.add_key(bit_string, i)
                bit_string = self.substitution(bit_string)
                bit_string = self.permutation(bit_string)
            bit_string = self.add_key(bit_string, self.rounds - 1)
            bit_string = self.substitution(bit_string)
            bit_string = self.add_key(bit_string, self.rounds)
            encryption += hc.bit_string_to_text(bit_string)
        return encryption
    
    def get_part_keys(self, ori, enc):
        """
        gets original as well as encrypted texts and returns the second and last key
        """
        enc = hc.hex_string_to_bit_string(enc)
        ori = hc.hex_string_to_bit_string(ori)
        
        # the algorithm is basically the same as the one from the slides
        # first part of the algorithm -> get the alphas
        alphas = [0 for _ in range(16 * 16)]
        for i in range(0, len(ori), 16):
            first_ori = ori[i + 4:i + 8]
            first_enc = enc[i + 4: i + 8]
            second_enc = enc[i + 12: i + 16]
            for l1 in range(0, 16):
                l1_bits = hc.int_to_bit_4(l1)
                v_2 = hc.xor_add(first_enc, l1_bits)
                u_2 = hc.int_to_bit_4(S_BOX.index(int(v_2, 2)))
                for l2 in range(0, 16):
                    l2_bits = hc.int_to_bit_4(l2)
                    v_4 = hc.xor_add(second_enc, l2_bits)
                    # S Box inverse
                    u_4 = hc.int_to_bit_4(S_BOX.index(int(v_4, 2)))

                    checking = [first_ori[0], first_ori[2], first_ori[3], u_2[1], u_2[3], u_4[1], u_4[3]]
                    if checking.count('1') % 2 == 0:
                        alphas[l1 * 16 + l2] += 1
        # second part of the algorithm -> find the key
        maxi = -1
        max_key = None
        length = len(ori) // 16
        for l1 in range(0, 16):
            for l2 in range(0, 16):
                beta = abs(alphas[l1 * 16 + l2] - (length / 2))
                if beta > maxi:
                    maxi = beta
                    max_key = (l1, l2)
        return max_key

    
if __name__ == "__main__":
    # text = ""
    # with open('input_break.txt') as f:
    #     text = f.read().replace("\n", " ")
    key = "b12f"
    # spn = SubstitutionPermutationNetwork(key)
    # enc = spn.encrypt(text)

    # print(spn.get_part_keys(text, enc))
    print('doing main???')


    with open('save_text.txt') as f:
        random_text = f.read()
    network = SubstitutionPermutationNetwork(key)
    encrypted = hc.bit_string_to_hex_string(hc.text_to_bit_string(network.encrypt(random_text, enc_hex=True)))
    with open('save_enc.txt', 'w') as f:
        f.write(encrypted)
