import helperclass as hc

class CTR:
    def __init__(self, key, initialisation=None, block_length=64) -> None:
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
        counter = 0
        for block in bit_blocks:
            res = self.encrypt_block(block, counter)
            encryption += res
            counter += 1

        return hc.bit_string_to_text(encryption)

    def encrypt_block(self, bit_string, counter):
        pass

    def decrypt_text(self, cipher_text):
        return self.encrypt_text(cipher_text)


if __name__ == "__main__":
    ctr = CTR("123", "123")

    enc = ctr.encrypt_text("Hallo Welt!asdasdd")
    print(enc)

    dec = ctr.decrypt_text(enc)
    print(dec)