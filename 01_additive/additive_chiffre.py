import helperclass as hc
import math


class AdditiveChiffre:
    def __init__(self, key=0) -> None:
        self.alphabet = hc.ALPHABET
        self.m = len(self.alphabet)
        self.key = key

    def encrypt_char(self, char):
        number = (hc.char_to_number(char) + self.key) % self.m
        return hc.number_to_char(number)

    def decrypt_char(self, char):
        number = (hc.char_to_number(char) - self.key) %  self.m
        return hc.number_to_char(number)
    
    def decrypt(self, input_file, output_file):
        content = hc.read_file(input_file)
        decrypt = self.decrypt_text(content)
        hc.write_file(decrypt, output_file)
        return 1

    def decrypt_text(self, content):
        decrypted_text = ""
        for char in content:
            if char in self.alphabet:
                decrypted_text += self.decrypt_char(char)
            else:
                decrypted_text += char
        return decrypted_text
    
    def encrypt(self, input_file, output_file):
        content = hc.read_file(input_file)
        encrypt = self.encrypt_text(content)
        hc.write_file(encrypt, output_file)
        return 1

    def encrypt_text(self, content):
        encrypted_text = ""
        for char in content:
            if char in self.alphabet:
                encrypted_text += self.encrypt_char(char)
            else:
                encrypted_text += char
        return encrypted_text
    
    def get_text_length(self, content):
        length = 0
        for char in content:
            length += 1 if char in self.alphabet else 0
        return length
    
    def break_chiffre(self, input_file, output_file):
        content = hc.read_file(input_file)
        key, decrypt = self.break_text(content)
        hc.write_file(f"{key}\n{decrypt}", output_file)
        return 1

    def break_text(self, content):
        text_length = self.get_text_length(content)

        min_loss = math.inf
        min_key = 0
        min_decrypted_text = ""
        for k in range(0, 26):
            loss = 0
            self.key = k
            decrypted_text = self.decrypt_text(content)

            char_count = [0 for _ in range(self.m)]
            for char in decrypted_text:
                if char in self.alphabet:
                    char_count[hc.char_to_number(char)] += 1

            for c in range(self.m):
                loss += (char_count[c] / text_length - hc.TRUE_VALUES[c])**2

            if loss < min_loss:
                min_decrypted_text = decrypted_text
                min_loss = loss
                min_key = k
        return min_key, min_decrypted_text



if __name__ == "__main__":
    c = AdditiveChiffre()
    c.encrypt_text("original.txt", 3, "encrypted.txt")
    