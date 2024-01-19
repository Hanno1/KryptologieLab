import helperclass as hc
from aes import AES
from aes_keygen import aes_keygen

class ECB:
    """
    encrypts / decrypts a text using the ecb blockchiffre algorithm given in the slides
    """
    def __init__(self, key, block_length = 128) -> None:
        self.key = key
        self.block_length = block_length
        # validate keys
        hc.check_aes_key(self.key, block_length)
        
        self.aes = AES()

    def get_blocks_of_bit_string(self, bit_string):
        # split the bit string into blocks of length block_length
        return [bit_string[i:i+self.block_length] for i in range(0, len(bit_string), self.block_length)]

    def encrypt_text(self, plain_text: str) -> str:
        """
        encrypts a text using the ecb blockchiffre algorithm given in the slides
        """
        # convert and split the bit string. Add a padding to the last block if necessary
        bit_content = hc.text_to_bit_string(plain_text)
        bit_blocks = self.get_blocks_of_bit_string(bit_content)
        while len(bit_blocks[-1]) < self.block_length:
            bit_blocks[-1] += "0"
        
        # encrypt every block
        encryption = ""
        for block in bit_blocks:
            encryption += self.encode_bit_block(block)
        return hc.bit_string_to_text(encryption)

    def encode_bit_block(self, bit_string):
        # just apply the aes algorithm encryption function
        return self.aes.encrypt(bit_string, self.key)
    
    def decrypt_text(self, cipher_text: str) -> str:
        """
        decrypts a text using the ecb blockchiffre algorithm given in the slides
        """
        # convert and split the bit string. Add a padding to the last block if necessary
        bit_content = hc.text_to_bit_string(cipher_text)
        bit_blocks = self.get_blocks_of_bit_string(bit_content)
        if len(bit_blocks[-1]) < self.block_length:
            return "Wrong Lenght of last block! Cant decode that!"
        
        # decrypt every block
        decryption = ""
        for block in bit_blocks:
            decryption += self.decode_bit_block(block)
        return hc.bit_string_to_text(decryption)

    def decode_bit_block(self, bit_string):
        # just apply the aes algorithm decryption function
        return self.aes.decrypt(bit_string, self.key)


if __name__ == "__main__":
    ecb = ECB()
    
    enc = ecb.encrypt_text("Hello World!12341234HDASDVASCccccccccccccccc")
    print(enc)

    dec = ecb.decrypt_text(enc)
    print(dec)
