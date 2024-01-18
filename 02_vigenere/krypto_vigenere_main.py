import helperclass as hc
import math

char_to_number = lambda char: ord(char) - 65
number_to_char = lambda number: chr(number + 65)

class Viginere:
    """
    class to handle the vigenere chiffre

    key: string with chars between A and Z
    """
    def __init__(self, key = None):
        self.key = key
        self.alphabet = hc.ALPHABET
        self.m = len(self.alphabet)

        self.encrypt_char = lambda char, k: number_to_char((char_to_number(char) + k) % self.m)
        self.decrypt_char = lambda char, k: number_to_char((char_to_number(char) - k) % self.m)

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

    def encrypt_text(self, text):
        """
        text: text to encrypt

        encrypts the text with the key self.key and returns it. The encryption is done with the vigenere chiffre
        """
        real_keys = [char_to_number(char) for char in self.key]
        encrypted_text = ""
        i = 0
        # iterate over every character in the text
        for char in text:
            if char in self.alphabet:
                # encrypt char with current key char and increment key index
                encrypted_text += self.encrypt_char(char, real_keys[i])
                i += 1
                if len(real_keys) == i:
                    i = 0
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

    def decrypt_text(self, text):
        """
        text: text to decrypt

        decrypts the text with the key self.key and returns it. The decryption is done with the vigenere chiffre
        """
        real_keys = [char_to_number(char) for char in self.key]
        decrypted_text = ""
        i = 0
        # iterate over every character in the text
        for char in text:
            if char in self.alphabet:
                # decrypt char with current key char and increment key index
                decrypted_text += self.decrypt_char(char, real_keys[i])
                i += 1
                if len(real_keys) == i:
                    i = 0
            else:
                decrypted_text += char
        return decrypted_text

    def break_vigenere_file(self, input_file, output_file):
        """
        input_file: path of the file with the text to decrypt
        output_file: path of the file to save the key and the decrypted text

        breaks the text in the input_file and save the result to the output_file
        """
        content = hc.read_file(input_file)
        key, decrypted = self.break_vigenere(content)
        hc.write_file(f"{key}\n{decrypted}", output_file)

    def break_vigenere(self, content):
        """
        computes the most probably key length n and then breaks the text as in the additive chiffre
        """
        n = self.break_chiffre_get_n(content)
        return self.break_chiffre(content, n)

    def break_chiffre_get_n(self, content):
        """
        content: text to break

        returns the most probable length of the key
        """
        cleaned_text = ""
        for char in content:
            if char in self.alphabet:
                cleaned_text += char
        # for keylength of 1 to 99
        for i in range(1, 100):
            texts = [cleaned_text[j::i] for j in range(i)]
            IC = 0
            for t in texts:
                ic = 1 / (len(t) * (len(t) - 1))
                ic *= (sum([(t.count(c) * (t.count(c) - 1)) for c in self.alphabet])) * (len(t) / len(cleaned_text))
                IC += ic
            # if the index of coincidence is close to 0.076 (the coincidence index of the german language), we found the key length
            if math.sqrt((IC - 0.076)**2) < 0.01:
                return i
        return -1
            
    def break_chiffre(self, original, n):
        """
        orginal: text to break
        n: length of the key

        basically additive break with n keys
        """
        # get all n keys and texts
        keys = [0 for _ in range(n)]
        texts = ["" for _ in range(n)]

        # generate texts
        i = 0
        for char in original:
            if char in self.alphabet:
                texts[i % n] += char
                i += 1
        
        # break every text and generate keys
        i = 0
        for t in texts:
            key, decrypted = self.break_additive(t)
            keys[i] = key
            texts[i] = decrypted
            i += 1

        # get the keystring
        key_string = ""
        for key in keys:
            key_string += number_to_char(key)

        # get the decryptet text
        return_text = ""
        i = 0
        j = 0
        for char in original:
            if char in self.alphabet:
                return_text += texts[i][j]
                i += 1
                if i == n:
                    i = 0
                    j += 1
            else:
                return_text += char

        # check key_string for multiple occurences of the same sequence        
        return hc.check_repeating_seq(key_string), return_text
    
    def decrypt_text_additive(self, content, k):
        """
        just an additive decryption as in the additive chiffre
        """
        decrypted_text = ""
        for char in content:
            if char in hc.ALPHABET:
                decrypted_text += self.decrypt_char(char, k)
            else:
                decrypted_text += char
        return decrypted_text
    
    def break_additive(self, content):
        """
        basically the same function as in the additive chiffre
        """
        text_length = hc.get_text_length(content)

        min_loss = math.inf
        min_key = 0
        min_decrypted_text = ""
        for k in range(0, 26):
            loss = 0

            decrypted_text = self.decrypt_text_additive(content, k)

            char_count = [0 for _ in range(self.m)]
            for char in decrypted_text:
                if char in self.alphabet:
                    char_count[char_to_number(char)] += 1

            for c in range(self.m):
                loss += (char_count[c] / text_length - hc.TRUE_VALUES[c])**2

            if loss < min_loss:
                min_decrypted_text = decrypted_text
                min_loss = loss
                min_key = k
        return min_key, min_decrypted_text



if __name__ == "__main__":
    text = "DIE ADDITIVE VERSCHLUESSELUNG, AUCH ALS CAESAR-CHIFFRE BEKANNT, IST EINE DER EINFACHSTEN UND AELTESTEN METHODEN ZUR VERSCHLUESSELUNG VON TEXTEN. BEI DIESER TECHNIK HANDELT ES SICH UM EINE VERSCHIEBECHIFFRE, BEI DER JEDER BUCHSTABE IM KLARTEXT UM EINE FESTE ANZAHL VON POSITIONEN IM ALPHABET VERSCHOBEN WIRD. DIESER VERSCHIEBUNGSPARAMETER WIRD ALS SCHLUESSEL BEZEICHNET UND IST AUSSCHLAGGEBEND FUER DEN VERSCHLUESSELUNGS- UND ENTSCHLUESSELUNGSVORGANG. BEISPIELSWEISE, WENN WIR DEN VERSCHIEBUNGSPARAMETER (SCHLUESSEL) AUF DREI FESTLEGEN, WIRD AUS DEM BUCHSTABEN A EIN D, AUS B WIRD E, UND SO WEITER. DIESER EINFACHE PROZESS KANN AUF DEN GESAMTEN KLARTEXT ANGEWENDET WERDEN, UM DEN GEHEIMTEXT ZU ERZEUGEN. DIE ENTSCHLUESSELUNG ERFOLGT, INDEM MAN DEN VERSCHIEBUNGSPARAMETER RUECKGAENGIG MACHT UND DIE URSPRUENGLICHEN BUCHSTABEN WIEDERHERSTELLT. OBWOHL DIE ADDITIVE VERSCHLUESSELUNG LEICHT ZU VERSTEHEN UND ANZUWENDEN IST, IST SIE NICHT BESONDERS SICHER, DA ES NUR SECHSUNDZWANZIG MOEGLICHE VERSCHIEBUNGSPARAMETER GIBT (DIE ANZAHL DER BUCHSTABEN IM ENGLISCHEN ALPHABET). DAS BEDEUTET, DASS EIN ANGREIFER RELATIV EINFACH ALLE MOEGLICHEN SCHLUESSEL DURCHPROBIEREN UND SOMIT DEN GEHEIMTEXT ENTSCHLUESSELN KANN. TROTZ IHRER GERINGEN SICHERHEIT WIRD DIE ADDITIVE VERSCHLUESSELUNG MANCHMAL ZU LEHRZWECKEN VERWENDET, UM GRUNDLEGENDE VERSCHLUESSELUNGSKONZEPTE ZU VERMITTELN. FUER EINE SICHERE KOMMUNIKATION IN DER MODERNEN WELT SIND JEDOCH KOMPLEXERE VERSCHLUESSELUNGSMETHODEN ERFORDERLICH, DIE AUF MATHEMATISCHEN ALGORITHMEN BASIEREN UND EINE DEUTLICH HOEHERE SICHERHEIT BIETEN."
    key = "BCFDGAFFF"

    V = Viginere(key=key)

    enc = V.encrypt_text(text)
    # print(enc)

    dec = V.decrypt_text(enc)
    # print(dec)

    l = V.break_chiffre_get_n(enc)
    print(l)

    key, l = V.break_vigenere(enc)
    print(key)

    print(hc.check_repeating_seq("BCDBCDBCDBCDA"))
