from aes import AES
import helperclass as hc 
import unittest
from aes_keygen import aes_keygen

from krypto_ecb_main import ECB
from krypto_cbc_main import CBC
from krypto_ofb_main import OFB
from krypto_ctr_main import CTR


EXAMPLE_KEYS = ["2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c",
"a0 fa fe 17 88 54 2c b1 23 a3 39 39 2a 6c 76 05",
"f2 c2 95 f2 7a 96 b9 43 59 35 80 7a 73 59 f6 7f",
"3d 80 47 7d 47 16 fe 3e 1e 23 7e 44 6d 7a 88 3b",
"ef 44 a5 41 a8 52 5b 7f b6 71 25 3b db 0b ad 00",
"d4 d1 c6 f8 7c 83 9d 87 ca f2 b8 bc 11 f9 15 bc",
"6d 88 a3 7a 11 0b 3e fd db f9 86 41 ca 00 93 fd",
"4e 54 f7 0e 5f 5f c9 f3 84 a6 4f b2 4e a6 dc 4f",
"ea d2 73 21 b5 8d ba d2 31 2b f5 60 7f 8d 29 2f",
"ac 77 66 f3 19 fa dc 21 28 d1 29 41 57 5c 00 6e",
"d0 14 f9 a8 c9 ee 25 89 e1 3f 0c c8 b6 63 0c a6"]


class TestAes(unittest.TestCase):
    def test_shift_rows(self):
        text = "AchtBuchstaben:)"
        bit_string_text = hc.text_to_bit_string(text)
        aes = AES()

        t1 = aes.shift_rows(bit_string_text, aes.shift_left)
        t2 = aes.shift_rows(t1, aes.shift_right)
        
        self.assertEqual(text, hc.bit_string_to_text(t2))

    def test_sub_bytes(self):
        text = "AchtBuchstaben:)"
        bit_string_text = hc.text_to_bit_string(text)
        aes = AES()

        t1 = aes.sub_bytes(bit_string_text, hc.SBOX)
        t2 = aes.sub_bytes(t1, hc.SBOX_INV)
        
        self.assertEqual(text, hc.bit_string_to_text(t2))

    def test_mix_columns(self):
        text = "AchtBuchstaben:)"
        bit_string_text = hc.text_to_bit_string(text)
        aes = AES()

        t1 = aes.mix_columns(bit_string_text, hc.MIX_COL)
        t2 = aes.mix_columns(t1, hc.MIX_COL_INV)
        
        self.assertEqual(text, hc.bit_string_to_text(t2))

    def test_keygen(self):
        single_key = EXAMPLE_KEYS[0].replace(" ", "")
        generated_keys = aes_keygen(single_key)

        for i in range(11):
            self.assertEqual(hc.bit_string_to_hex_string(generated_keys[i]), EXAMPLE_KEYS[i].replace(" ", ""))

    def test_aes_full(self):
        klar_hex = "5c f6 ee 79 2c df 05 e1 ba 2b 63 25 c4 1a 5f 10".replace(" ", "")
        krypto_hex = "e2 48 89 ba aa dd 90 6b 06 30 06 59 8b 8c e4 59".replace(" ", "")
        key = "2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c".replace(" ", "")

        keys = aes_keygen(key)
        aes = AES()

        encryption = aes.encrypt(hc.hex_string_to_bit_string(klar_hex), keys)
        self.assertEqual(hc.bit_string_to_hex_string(encryption), krypto_hex)

        decryption = aes.decrypt(encryption, keys)
        self.assertEqual(hc.bit_string_to_hex_string(decryption), klar_hex)

    def test_ecb(self):
        key = "2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c".replace(" ", "")
        keys = aes_keygen(key)

        ecb = ECB(keys)
        original = "Hallo Welt!This is a test\n gernerated"
        encryption = ecb.encrypt_text("Hallo Welt!This is a test\n gernerated")
        decryption = ecb.decrypt_text(encryption)

        self.assertEqual(original, decryption.replace("\x00", ""))

    def test_cbc(self):
        key = "2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c".replace(" ", "")
        keys = aes_keygen(key)
        init_vec = "d4 d1 4c 15 ee a3 e8 e5 bd 7a bd ea ee d8 c0 b5".replace(" ", "")

        cbc = CBC(initialisation=hc.hex_string_to_bit_string(init_vec), key=keys)
        original = "Hallo Welt!This is a test\n gernerated"
        encryption = cbc.encrypt_text("Hallo Welt!This is a test\n gernerated")
        decryption = cbc.decrypt_text(encryption)

        self.assertEqual(original, decryption.replace("\x00", ""))

    def test_ofb(self):
        key = "2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c".replace(" ", "")
        keys = aes_keygen(key)
        init_vec = "d4 d1 4c 15 ee a3 e8 e5 bd 7a bd ea ee d8 c0 b5".replace(" ", "")

        ofb = OFB(initialisation=hc.hex_string_to_bit_string(init_vec), key=keys)
        original = "Hallo Welt!This is a test\n gernerated"
        encryption = ofb.encrypt_text("Hallo Welt!This is a test\n gernerated")
        decryption = ofb.decrypt_text(encryption)

        self.assertEqual(original, decryption.replace("\x00", ""))

    def test_ctr(self):
        key = "2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c".replace(" ", "")
        keys = aes_keygen(key)

        ctr = CTR(key=keys)
        original = "Hallo Welt!This is a test\n gernerated"
        encryption = ctr.encrypt_text("Hallo Welt!This is a test\n gernerated")
        decryption = ctr.decrypt_text(encryption)

        self.assertEqual(original, decryption.replace("\x00", ""))

if __name__ == "__main__":
    unittest.main()