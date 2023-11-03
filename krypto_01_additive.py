import helperclass as hc
import math


def encrypt_char(char, key):
    number = (hc.char_to_number(char) + key) % hc.M
    return hc.number_to_char(number)

def decrypt_char(char, key):
    number = (hc.char_to_number(char) - key) %  hc.M
    return hc.number_to_char(number)

def encrypt_file(input_file, output_file, key):
    content = hc.read_file(input_file)
    encrypt = encrypt_text(content, key)
    hc.write_file(encrypt, output_file)
    return 1

def encrypt_text(content, key):
    encrypted_text = ""
    for char in content:
        if char in hc.ALPHABET:
            encrypted_text += encrypt_char(char, key)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_file(input_file, output_file, key):
    content = hc.read_file(input_file)
    decrypt = decrypt_text(content, key)
    hc.write_file(decrypt, output_file)
    return 1

def decrypt_text(content, key):
    decrypted_text = ""
    for char in content:
        if char in hc.ALPHABET:
            decrypted_text += decrypt_char(char, key)
        else:
            decrypted_text += char
    return decrypted_text

def break_additive_file(input_file, output_file):
    content = hc.read_file(input_file)
    key, decrypt = break_additive(content)
    hc.write_file(f"{key}\n{decrypt}", output_file)
    return 1

def break_additive(content):
    text_length = hc.get_text_length(content)

    min_loss = math.inf
    min_key = 0
    min_decrypted_text = ""
    for k in range(0, 26):
        loss = 0
        decrypted_text = decrypt_text(content, k)

        char_count = [0 for _ in range(hc.M)]
        for char in decrypted_text:
            if char in hc.ALPHABET:
                char_count[hc.char_to_number(char)] += 1

        for c in range(hc.M):
            loss += (char_count[c] / text_length - hc.TRUE_VALUES[c])**2

        if loss < min_loss:
            min_decrypted_text = decrypted_text
            min_loss = loss
            min_key = k
    return min_key, min_decrypted_text


if __name__ == "__main__":
    encrypt_file("01_additive/original.txt", "01_additive/encrypted.txt", 3)
    decrypt_file("01_additive/encrypted.txt", "01_additive/decrypted.txt", 3)
    break_additive_file("01_additive/sampleEncrypted.txt", "01_additive/sampleDecrypted.txt")
