import helperclass as hc
import copy

class OFB:
    def __init__(self, key, initialisation, block_length=64) -> None:
        self.key = key
        self.iv = initialisation
        self.block_length = block_length

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
        pass
        tmp_result = copy.deepcopy(last_bit_string)

        # 2. add tmp_result and the plaintext
        new_bit_string = ""
        for i in range(self.block_length):
            new_bit_string += str(int(bit_string[i]) ^ int(tmp_result[i]))
        return new_bit_string, tmp_result

    def decrypt_text(self, cipher_text):
        return self.encrypt_text(cipher_text)


if __name__ == "__main__":
    iv = ""
    for i in range(64):
        # if i == 10 or i == 11 or i == 13 or i == 61:
        #     iv += "1"
        #     continue
        iv += "0"

    ofb = OFB("123", iv)

    enc = ofb.encrypt_text("Hallo Welt!asdasdd")
    print(enc)

    dec = ofb.decrypt_text(enc)
    print(dec)
