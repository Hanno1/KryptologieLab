import helperclass as hc
from aes import AES

class CBC:
    """
    implements the cbc blockchiffre using the aes algorithm for encrypting / decrypting blocks
    """
    def __init__(self, initialisation, key, block_length=128):
        self.key = key
        self.block_length = block_length
        # validate keys
        hc.check_aes_key(self.key, self.block_length)

        self.aes = AES()

        self.iv = initialisation
        if len(self.iv) != self.block_length:
            raise Exception("Wrong length of initialisation vector! It has to be " + str(self.block_length) + " but is " + str(len(self.iv)))

    def get_blocks_of_bit_string(self, bit_string):
        # split the bit string into blocks of length block_length
        return [bit_string[i:i+self.block_length] for i in range(0, len(bit_string), self.block_length)]

    def encrypt_text(self, plain_text):
        """
        encrypts a text using the cbc blockchiffre algorithm given in the slides
        """
        # convert and split the bit string. Add a padding to the last block if necessary
        bit_content = hc.text_to_bit_string(plain_text)
        bit_blocks = self.get_blocks_of_bit_string(bit_content)
        while len(bit_blocks[-1]) < self.block_length:
            bit_blocks[-1] += "0"

        encryption = ""
        last_bit_string = self.iv

        # encrypt every block using the cbc algorithm and the aes encryption 
        for block in bit_blocks:
            res = self.encrypt_block(block, last_bit_string)
            encryption += res
            last_bit_string = res

        return hc.bit_string_to_text(encryption)

    def encrypt_block(self, bit_string, last_bit_string):
        """
        encrypts a single block using the cbc algorithm -> first add last bitstring to x_i and then encrypt it using aes
        """
        # 1. add E(x_i-1) to x_i
        new_bit_string = ""
        for i in range(self.block_length):
            new_bit_string += str(int(bit_string[i]) ^ int(last_bit_string[i]))
        # 2. normal encode
        return self.aes.encrypt(new_bit_string, self.key)

    def decrypt_text(self, cipher_text):
        """
        decrypts a text using the cbc blockchiffre algorithm given in the slides 
        -> basically encryption but uses decrypt block instead of encrypt block
        """
        bit_content = hc.text_to_bit_string(cipher_text)
        bit_blocks = self.get_blocks_of_bit_string(bit_content)
        if len(bit_blocks[-1]) != self.block_length:
            raise Exception("Last block length is not right!")

        decryption = ""
        last_bit_string = self.iv

        # decrypt the block of length block length
        for block in bit_blocks:
            res = self.decrypt_block(block, last_bit_string)
            decryption += res
            last_bit_string = block

        return hc.bit_string_to_text(decryption)

    def decrypt_block(self, bit_string, last_bit_string):
        """
        encryption backward -> first decrypt with the aes and then add the previous result
        """
        # 1. normal encode
        bit_string = self.aes.decrypt(bit_string, self.key)

        # 2. add D(x_i-1) to x_i
        new_bit_string = ""
        for i in range(self.block_length):
            new_bit_string += str(int(bit_string[i]) ^ int(last_bit_string[i]))
        
        return new_bit_string


if __name__ == "__main__":
    iv = "0" * 128
    cbc = CBC(iv)

    enc = cbc.encrypt_text("Hello World Ich bin Hanno und das ist ein Test!")
    print(enc)

    dec = cbc.decrypt_text(enc)
    print(dec)
