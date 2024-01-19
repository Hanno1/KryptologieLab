import helperclass as hc
import copy
from aes import AES

class OFB:
    """
    encrypts / decrypts a text using the ofb blockchiffre algorithm given in the slides
    """
    def __init__(self, initialisation, key, block_length=128) -> None:
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
        encrypts a text using the ofb blockchiffre algorithm given in the slides
        """
        # convert and split the bit string. Add a padding to the last block if necessary
        bit_content = hc.text_to_bit_string(plain_text)
        bit_blocks = self.get_blocks_of_bit_string(bit_content)
        while len(bit_blocks[-1]) < self.block_length:
            bit_blocks[-1] += "0"
        
        # encrypt every block
        encryption = ""
        last_bit_string = self.iv
        for block in bit_blocks:
            res, new_last_bit_string = self.encrypt_block(block, last_bit_string)
            encryption += res
            last_bit_string = new_last_bit_string

        return hc.bit_string_to_text(encryption)

    def encrypt_block(self, bit_string, last_bit_string):
        """
        encrypts a single block using the ofb algorithm -> first encrypt the last bit string and then add it to the plaintext
        """
        # 1. normal encode using the key and the last bit string
        tmp_result = copy.deepcopy(last_bit_string)
        tmp_result = self.aes.encrypt(tmp_result, self.key)

        # 2. add tmp_result and the plaintext
        return hc.xor_add(bit_string, tmp_result), tmp_result

    def decrypt_text(self, cipher_text):
        """
        decryption is the same as encryption in the ofb algorithm
        """
        return self.encrypt_text(cipher_text)


if __name__ == "__main__":
    iv = "0" * 128

    ofb = OFB(iv)

    enc = ofb.encrypt_text("Hallo Welt!asdasdd")
    print(enc)

    dec = ofb.decrypt_text(enc)
    print(dec)
