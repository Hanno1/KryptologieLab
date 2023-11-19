from aes import AES
import helperclass as hc 
import unittest


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


if __name__ == "__main__":
    unittest.main()