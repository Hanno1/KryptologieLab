import helperclass as hc
import copy


class AES:
    """
    AES algorithm. Its a class to group all functionalities together. It could be implemented as single functions as well.
    """
    def __init__(self):
        pass

    def encrypt(self, bit_string, keys):
        """
        encrypts a bitstring given 11 keys using the aes algorithm
        """
        # 128 bit string, 11 keys
        current_bit_string = bit_string
        current_bit_string = hc.xor_add(current_bit_string, keys[0])
        for i in range(1, 10):
            current_bit_string = self.sub_bytes(current_bit_string, hc.SBOX)
            current_bit_string = self.shift_rows(current_bit_string, self.shift_left)
            current_bit_string = self.mix_columns(current_bit_string, hc.MIX_COL)
            current_bit_string = hc.xor_add(current_bit_string, keys[i])

        current_bit_string = self.sub_bytes(current_bit_string, hc.SBOX)
        current_bit_string = self.shift_rows(current_bit_string, self.shift_left)
        current_bit_string = hc.xor_add(current_bit_string, keys[10])

        return current_bit_string

    def decrypt(self, bit_string, keys):
        """
        decrypts a bitstring given 11 keys. Its just the inverse of the encrypt function and inverse keyorder
        """
        current_bit_string = bit_string

        current_bit_string = hc.xor_add(current_bit_string, keys[10])
        current_bit_string = self.shift_rows(current_bit_string, self.shift_right)
        current_bit_string = self.sub_bytes(current_bit_string, hc.SBOX_INV)

        for i in range(1, 10):
            current_bit_string = hc.xor_add(current_bit_string, keys[10 - i])
            current_bit_string = self.mix_columns(current_bit_string, hc.MIX_COL_INV)
            current_bit_string = self.shift_rows(current_bit_string, self.shift_right)
            current_bit_string = self.sub_bytes(current_bit_string, hc.SBOX_INV)
            
        current_bit_string = hc.xor_add(current_bit_string, keys[0])

        return current_bit_string

    def sub_bytes(self, bit_string, sbox):
        """
        applies the sub bytes function of the aes. It takes the sbox from the helperclass and applies it to the bitstring
        This function can be used for the inverse as well, since only the sbox changes to the inverse sbox
        """
        text = hc.bit_string_to_text(bit_string)
        new_text = ""
        # take each character and apply the sbox -> 8 bytes to 8 bytes
        for char in text:
            new_text += chr(sbox[ord(char)])
        # convert back to bitstring
        new_bit_string = hc.text_to_bit_string(new_text)
        return new_bit_string
    
    def shift_left(self, bit_list):
        """
        shifts a list of bits one step to the left
        """
        new_list = copy.deepcopy(bit_list)
        tmp = new_list.pop(0)
        new_list.append(tmp)
        return new_list
    
    def shift_right(self, bit_list):
        """
        shifts a list of bits one step to the right
        """
        new_list = copy.deepcopy(bit_list)
        tmp = new_list.pop(-1)
        new_list.insert(0, tmp)
        return new_list

    def shift_rows(self, bit_string, function):
        """
        shift rows function of the aes. It goes through every row and shifts it by the row index
        """
        # first get the actual rows -> 4 rows with 4 bytes each
        rows = []
        for i in range(4):
            row = []
            # get the row j
            for j in range(4):
                # get the corresponding byte of the row j and the column i
                row.append(bit_string[4 * 8 * j + i * 8: 4 * 8 * j + i * 8 + 8])
            # shift the row using either a left or a right shift (function = shift_left or shift_right)
            for _ in range(i):
                row = function(row)
            rows.append(row)
        # now put the rows back together
        new_bit_string = ""
        for row in range(4):
            for col in range(4):
                new_bit_string += rows[col][row]
        return new_bit_string  
    
    def mix_columns(self, bit_string, mat):
        """
        implements the mix columns function of the aes. It is implemented using matrixmultiplication in GF(2^8)
        it takes every 32 bits and applies the algorithm given in the slides. basically addition and multiplication in GF(2^8)
        """
        # take 32 bits for one mixcolumns
        new_bit_string = ""
        for col in range(4):
            # take col-th column
            current_bit_string = bit_string[col * 32: col * 32 + 32]
            new_bits = ["0"*8 for _ in range(4)]
            for entry in range(4):
                # take byte part of entry, multiply it and then add it to new bits
                relevant_entry = current_bit_string[entry * 8: entry * 8 + 8]
                for i in range(4):
                    # actual computation:
                    # gets the multiplier from the current byte
                    multiplier = hc.int_to_byte(mat[i][entry])[::-1]
                    # computes the result of the multiplication modulo the polynom x^8 + x^4 + x^3 + x + 1	
                    result = self.mix_columns_compute(relevant_entry, multiplier)
                    # add them using xor as stated in the slides
                    new_bits[i] = hc.xor_add(new_bits[i], result)
            for j in range(4):
                new_bit_string += new_bits[j]
        return new_bit_string

    def mix_columns_compute(self, byte_string, multiplier):
        """
        multiplication in GF(2^8). doubles the bit string as often as the multiplier says and then adds them together
        """
        result_bit_string = "0"*8
        for b in range(4):
            if multiplier[b] == "1":
                new_bit_string = copy.deepcopy(byte_string)
                for _ in range(b):
                    new_bit_string = self.double(new_bit_string)
                result_bit_string = hc.xor_add(result_bit_string, new_bit_string)
        return result_bit_string
    
    def double(self, bit_string):
        """
        will double the bitstring one time in GF(2^8) using the algorithm given in the slides
        """
        orig = copy.deepcopy(bit_string)
        # double is just a left shift
        bit_string = bit_string[1:]
        bit_string += "0"
        if orig[0] == "1":
            bit_string = hc.xor_add(bit_string, "00011011")
        return bit_string


if __name__ == "__main__":
    # read key
    keys = hc.read_key_from_file("Beispiel_key.txt")
    with open("Beispiel_1_Klartext.txt") as f:
        content = f.read().replace("\n", "").replace(" ", "")
    bit_string = hc.hex_string_to_bit_string(content)

    aes = AES()
    print(hc.bit_string_to_hex_string(bit_string))

    enc = aes.encrypt(bit_string, keys)
    print(hc.bit_string_to_hex_string(enc))

    dec = aes.decrypt(enc, keys)
    print(hc.bit_string_to_hex_string(dec))
