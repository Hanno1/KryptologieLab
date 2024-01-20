import helperclass as hc
from aes import AES

class CTR:
    """
    implements the ctr blockchiffre using the aes algorithm for encrypting / decrypting blocks
    """
    def __init__(self, key, block_length=128):
        self.key = key
        self.block_length = block_length
        # validate keys
        hc.check_aes_key(self.key, self.block_length)

        self.aes = AES()

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
        
        # encrypt every block
        encryption = ""
        counter = 0
        for block in bit_blocks:
            encryption += self.encrypt_block(block, counter)
            counter += 1

        return hc.bit_string_to_text(encryption)

    def encrypt_block(self, bit_string, counter):
        """
        encrypt single block just by using the aes and Xor adding the counter as in slides
        """
        counter_bit_string = bin(counter)[2:].zfill(self.block_length)
        return hc.xor_add(self.aes.encrypt(counter_bit_string, self.key), bit_string)

    def decrypt_text(self, cipher_text):
        """
        decryption is just encryption in the ctr algorithm
        """
        return self.encrypt_text(cipher_text)


if __name__ == "__main__":
    ctr = CTR()

    enc = ctr.encrypt_text("Hallo Welt!asdasddFFFFFFFasdffasdcccKKKKKKKKKKKHalloWelt!asdasddFFFFFFFasdffasdcccKKKKKKKKKKK")
    print(enc)

    dec = ctr.decrypt_text(enc)
    print(dec)