import helperclass as hc
from aes import AES
from aes_keygen import aes_keygen

class CTR:
    def __init__(self, key=None, block_length=128) -> None:
        self.key = key
        self.block_length = block_length

        if key is None:
            self.key = aes_keygen(hc.read_key_from_file("key.txt"))
        hc.check_aes_key(self.key, self.block_length)
        self.aes = AES()

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
            encryption += self.encrypt_block(block, counter)
            counter += 1

        return hc.bit_string_to_text(encryption)

    def encrypt_block(self, bit_string, counter):
        # counter to bit string
        # counter = counter % (2**self.block_length)
        counter_bit_string = bin(counter)[2:].zfill(self.block_length)
        return hc.xor_add(self.aes.encrypt(counter_bit_string, self.key), bit_string)

    def decrypt_text(self, cipher_text):
        return self.encrypt_text(cipher_text)


if __name__ == "__main__":
    ctr = CTR()

    enc = ctr.encrypt_text("Hallo Welt!asdasddFFFFFFFasdffasdcccKKKKKKKKKKKHalloWelt!asdasddFFFFFFFasdffasdcccKKKKKKKKKKK")
    print(enc)

    dec = ctr.decrypt_text(enc)
    print(dec)