import helperclass as hc
import copy
from aes import AES

class OFB:
    def __init__(self, initialisation, key=None, block_length=128) -> None:
        self.key = key
        self.block_length = block_length
        if key is None:
            self.key = hc.read_key_from_file("Beispiel_key.txt")
        hc.check_aes_key(self.key, self.block_length)
        self.aes = AES()
        self.iv = initialisation
        if len(self.iv) != self.block_length:
            raise Exception("Wrong length of initialisation vector! It has to be " + str(self.block_length) + " but is " + str(len(self.iv)))

    def get_blocks_of_bit_string(self, bit_string):
        return [bit_string[i:i+self.block_length] for i in range(0, len(bit_string), self.block_length)]
    
    def encrypt_text(self, plain_text): 
        bit_content = hc.text_to_bit_string(plain_text)
        bit_blocks = self.get_blocks_of_bit_string(bit_content)
        while len(bit_blocks[-1]) < self.block_length:
            bit_blocks[-1] += "0"
        
        encryption = ""
        last_bit_string = self.iv

        for block in bit_blocks:
            res, new_last_bit_string = self.encrypt_block(block, last_bit_string)
            encryption += res
            last_bit_string = new_last_bit_string

        return hc.bit_string_to_text(encryption)

    def encrypt_block(self, bit_string, last_bit_string):
        # 1. normal encode using the key and the last bit string
        tmp_result = copy.deepcopy(last_bit_string)
        tmp_result = self.aes.encrypt(tmp_result, self.key)

        # 2. add tmp_result and the plaintext
        new_bit_string = ""
        for i in range(self.block_length):
            new_bit_string += str(int(bit_string[i]) ^ int(tmp_result[i]))
        return new_bit_string, tmp_result

    def decrypt_text(self, cipher_text):
        return self.encrypt_text(cipher_text)


if __name__ == "__main__":
    iv = "0" * 128

    ofb = OFB(iv)

    enc = ofb.encrypt_text("Hallo Welt!asdasdd")
    print(enc)

    dec = ofb.decrypt_text(enc)
    print(dec)
