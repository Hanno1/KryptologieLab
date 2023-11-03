from helperclass import ALPHABET, char_to_number, number_to_char, read_file, write_file
from krypto_01_additive import encrypt_char, decrypt_char, break_additive
import math
from sklearn.cluster import KMeans


def encrypt_file(input_file, output_file, keys):
    content = read_file(input_file)
    encrypt = encrypt_text(content, keys)
    write_file(encrypt, output_file)
    return 1

def encrypt_text(text, keys):
    real_keys = [char_to_number(char) for char in keys]
    encrypted_text = ""
    i = 0
    for char in text:
        if char in ALPHABET:
            encrypted_text += encrypt_char(char, real_keys[i])
            i += 1
            if len(real_keys) == i:
                i = 0
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_file(input_file, output_file, keys):
    content = read_file(input_file)
    decrypt = decrypt_text(content, keys)
    write_file(decrypt, output_file)
    return 1

def decrypt_text(text, keys):
    real_keys = [char_to_number(char) for char in keys]
    decrypted_text = ""
    i = 0
    for char in text:
        if char in ALPHABET:
            decrypted_text += decrypt_char(char, real_keys[i])
            i += 1
            if len(real_keys) == i:
                i = 0
        else:
            decrypted_text += char
    return decrypted_text

def break_vigenere_file(input_file, output_file):
    content = read_file(input_file)
    key, decrypted = break_vigenere(content)
    write_file(f"{key}\n{decrypted}", output_file)

def break_vigenere(content):
    n = break_chiffre_get_n(content)
    return break_chiffre(content, n)

def break_chiffre_get_n(content):
    cleaned_text = ""
    for char in content:
        if char in ALPHABET:
            cleaned_text += char
    ICs = []
    for i in range(1, 100):
        texts = [cleaned_text[j::i] for j in range(i)]
        IC = 0
        for t in texts:
            ic = 1 / (len(t) * (len(t) - 1))
            ic *= (sum([(t.count(c) * (t.count(c) - 1)) for c in ALPHABET])) * (len(t) / len(cleaned_text))
            IC += ic
        ICs.append([0, IC])
    kmeans = KMeans(n_clusters=2, n_init=10).fit(ICs)
    centers = kmeans.cluster_centers_
    dist1 = math.sqrt((centers[0][1] - 0.076)**2)
    dist2 = math.sqrt((centers[1][1] - 0.076)**2)

    labels = list(kmeans.labels_)
    if dist1 < dist2:
        # take position of first label 1
        return (labels.index(0) + 1)
    else:
        return (labels.index(1) + 1)
        
def break_chiffre(original, n):
    keys = [0 for _ in range(n)]
    texts = ["" for _ in range(n)]

    i = 0
    for char in original:
        if char in ALPHABET:
            texts[i % n] += char
            i += 1
    
    i = 0
    for t in texts:
        key, decrypted = break_additive(t)
        keys[i] = key
        texts[i] = decrypted
        i += 1

    key_string = ""
    for key in keys:
        key_string += number_to_char(key)

    return_text = ""
    i = 0
    j = 0
    for char in original:
        if char in ALPHABET:
            return_text += texts[i][j]
            i += 1
            if i == n:
                i = 0
                j += 1
        else:
            return_text += char

    return key_string, return_text



if __name__ == "__main__":
    text = "DIE ADDITIVE VERSCHLUESSELUNG, AUCH ALS CAESAR-CHIFFRE BEKANNT, IST EINE DER EINFACHSTEN UND AELTESTEN METHODEN ZUR VERSCHLUESSELUNG VON TEXTEN. BEI DIESER TECHNIK HANDELT ES SICH UM EINE VERSCHIEBECHIFFRE, BEI DER JEDER BUCHSTABE IM KLARTEXT UM EINE FESTE ANZAHL VON POSITIONEN IM ALPHABET VERSCHOBEN WIRD. DIESER VERSCHIEBUNGSPARAMETER WIRD ALS SCHLUESSEL BEZEICHNET UND IST AUSSCHLAGGEBEND FUER DEN VERSCHLUESSELUNGS- UND ENTSCHLUESSELUNGSVORGANG. BEISPIELSWEISE, WENN WIR DEN VERSCHIEBUNGSPARAMETER (SCHLUESSEL) AUF DREI FESTLEGEN, WIRD AUS DEM BUCHSTABEN A EIN D, AUS B WIRD E, UND SO WEITER. DIESER EINFACHE PROZESS KANN AUF DEN GESAMTEN KLARTEXT ANGEWENDET WERDEN, UM DEN GEHEIMTEXT ZU ERZEUGEN. DIE ENTSCHLUESSELUNG ERFOLGT, INDEM MAN DEN VERSCHIEBUNGSPARAMETER RUECKGAENGIG MACHT UND DIE URSPRUENGLICHEN BUCHSTABEN WIEDERHERSTELLT. OBWOHL DIE ADDITIVE VERSCHLUESSELUNG LEICHT ZU VERSTEHEN UND ANZUWENDEN IST, IST SIE NICHT BESONDERS SICHER, DA ES NUR SECHSUNDZWANZIG MOEGLICHE VERSCHIEBUNGSPARAMETER GIBT (DIE ANZAHL DER BUCHSTABEN IM ENGLISCHEN ALPHABET). DAS BEDEUTET, DASS EIN ANGREIFER RELATIV EINFACH ALLE MOEGLICHEN SCHLUESSEL DURCHPROBIEREN UND SOMIT DEN GEHEIMTEXT ENTSCHLUESSELN KANN. TROTZ IHRER GERINGEN SICHERHEIT WIRD DIE ADDITIVE VERSCHLUESSELUNG MANCHMAL ZU LEHRZWECKEN VERWENDET, UM GRUNDLEGENDE VERSCHLUESSELUNGSKONZEPTE ZU VERMITTELN. FUER EINE SICHERE KOMMUNIKATION IN DER MODERNEN WELT SIND JEDOCH KOMPLEXERE VERSCHLUESSELUNGSMETHODEN ERFORDERLICH, DIE AUF MATHEMATISCHEN ALGORITHMEN BASIEREN UND EINE DEUTLICH HOEHERE SICHERHEIT BIETEN."
    keys = "BCFDGAFFF"

    enc = encrypt_text(text, keys)
    # print(enc)

    dec = decrypt_text(enc, keys)
    # print(dec)

    # l = viginere.break_text_wihhout_n(enc)
    # print(l)
    # print(viginere.break_chiffre(enc, l))

    key, l = break_vigenere(enc)
    print(key)
