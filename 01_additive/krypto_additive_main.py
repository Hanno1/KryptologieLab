import helperclass as hc
import math

char_to_number = lambda char: ord(char) - 65
number_to_char = lambda number: chr(number + 65)


class Additive_Chiffre:
    """
    Class to encrypt, decrypt and break additive chiffre
    """
    def __init__(self, key=None) -> None:
        """
        key: letter of the alphabet between 0 and 25, the key will be used for encryption and decryption
        encrypt_char: function to encrypt a single character -> ascii to 0-25
        decrypt_char: function to decrypt a single character -> 0-25 to ascii
        """
        if key is not None:
            self.key = key % 26
        self.key = key
        self.alphabet = hc.ALPHABET
        self.m = len(self.alphabet)

        self.encrypt_char = lambda char: char
        self.decrypt_char = lambda char: char

        if key is not None:
            self.define_key_functions()

    def define_key_functions(self):
        self.encrypt_char = lambda char: number_to_char((char_to_number(char) + self.key) % self.m)
        self.decrypt_char = lambda char: number_to_char((char_to_number(char) - self.key) % self.m)

    def encrypt_file(self, input_file, output_file):
        """
        input_file: path of the file with the text to encrypt
        output_file: path of the file to save the encrypted text

        encrypts the text in the input_file and saves it in the output_file
        """
        content = hc.read_file(input_file)
        encrypt = self.encrypt_text(content)
        hc.write_file(encrypt, output_file)
        return 1

    def encrypt_text(self, content):
        """
        content: text to encrypt

        encrypts the text with the key self.key and returns it
        """
        encrypted_text = ""
        for char in content:
            if char in self.alphabet:
                encrypted_text += self.encrypt_char(char)
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt_file(self, input_file, output_file):
        """
        input_file: path of the file with the text to decrypt
        output_file: path of the file to save the decrypted text

        decrypts the text in the input_file and saves it in the output_file
        """
        content = hc.read_file(input_file)
        decrypt = self.decrypt_text(content)
        hc.write_file(decrypt, output_file)
        return 1

    def decrypt_text(self, content):
        """
        content: text to decrypt

        decrypts the text with the key self.key and returns it
        """
        decrypted_text = ""
        for char in content:
            if char in hc.ALPHABET:
                decrypted_text += self.decrypt_char(char)
            else:
                decrypted_text += char
        return decrypted_text

    def break_additive_file(self, input_file, output_file):
        """
        input_file: path of the file with the encryptet text to break
        output_file: path of the file to save the key and the decrypted text

        breaks the additive chiffre and saves the key and the decrypted text in the output_file
        """
        content = hc.read_file(input_file)
        key, decrypt = self.break_additive(content)
        hc.write_file(f"{key}\n{decrypt}", output_file)
        return 1

    def break_additive(self, content):
        """
        content: text to break

        breaks the additive chiffre and returns the key and the decrypted text. The breaking is implemented as in the slides.
        """
        text_length = hc.get_text_length(content)

        min_loss = math.inf
        min_key = 0
        min_decrypted_text = ""

        # iterate over every possible key 0 - 25
        for k in range(0, 26):
            loss = 0
            self.key = k
            self.define_key_functions()

            decrypted_text = self.decrypt_text(content)
            
            # calculate the frequency of each character
            char_count = [0 for _ in range(self.m)]
            for char in decrypted_text:
                if char in self.alphabet:
                    char_count[char_to_number(char)] += 1
            
            # compute the loss against the real frequencies in the german language
            for c in range(self.m):
                loss += (char_count[c] / text_length - hc.TRUE_VALUES[c])**2

            if loss < min_loss:
                min_decrypted_text = decrypted_text
                min_loss = loss
                min_key = k
        return min_key, min_decrypted_text


if __name__ == "__main__":
    additive = Additive_Chiffre(key = 3)

    additive.encrypt_file("original.txt", "encrypted.txt")
    additive.decrypt_file("encrypted.txt", "decrypted.txt")
    additive.break_additive_file("sampleEncrypted.txt", "sampleDecrypted.txt")
