import helperclass as hc

S_BOX = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]
PERMUTATION = [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]

class SubstitutionPermutationNetwork:
    def __init__(self, key) -> None:
        self.block_length = 16
        self.rounds = 4
        key = hc.hex_string_to_bit_string(key)
        self.keys = [key for _ in range(self.rounds + 1)]

    def get_blocks_of_bit_string(self, bit_string):
        return [bit_string[i:i+self.block_length] for i in range(0, len(bit_string), self.block_length)]

    def add_key(self, bit_string, round):
        return hc.xor_add(bit_string, self.keys[round])
    
    def substitution(self, bit_string):
        new_bit_string = ""
        for i in range(0, len(bit_string), 4):
            new_bit_string += hc.int_to_bit_4(S_BOX[int(bit_string[i:i+4], 2)])
        return new_bit_string
    
    def permutation(self, bit_string):
        new_bits = [0 for _ in range(len(bit_string))]
        for i in range(0, len(bit_string)):
            new_bits[PERMUTATION[i] - 1] = bit_string[i]
        return ''.join(new_bits)

    def encrypt(self, plaintext):
        bit_content = hc.text_to_bit_string(plaintext)
        bit_blocks = self.get_blocks_of_bit_string(bit_content)
        while len(bit_blocks[-1]) < self.block_length:
            bit_blocks[-1] += "0"
        encryption = ""
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

    def decrypt(self, ciphertext):
        # bit_content = hc.text_to_bit_string(ciphertext)
        # bit_blocks = self.get_blocks_of_bit_string(bit_content)

        # encryption = ""
        # for bit_string in bit_blocks:
        #     bit_string = self.add_key(bit_string, self.rounds)
        #     bit_string = self.substitution(bit_string)
        #     bit_string = self.add_key(bit_string, self.rounds - 1)
        #     for i in range(self.rounds - 2, -1, -1):
        #         bit_string = self.permutation(bit_string)
        #         bit_string = self.substitution(bit_string)
        #         bit_string = self.add_key(bit_string, i)
        #     encryption += hc.bit_string_to_text(bit_string)
        # return encryption
        return -1

    
if __name__ == "__main__":
    text = "Hallo Welt!"
    key = "abcd"
    spn = SubstitutionPermutationNetwork(key)
    enc = spn.encrypt(text)
    print("Encryption: ", enc)
