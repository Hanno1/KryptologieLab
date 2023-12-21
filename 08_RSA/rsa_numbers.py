import helperclass as hc

def quad_and_mult(x, n, m):
    y = 1
    m_bit = hc.int_to_bit(m)[::-1]
    for i in range(len(m_bit)):
        if m_bit[i] == '1':
            y = y * x % n
        x = x**2 % n
    return y

def rsa_alg(key, text):
    e,n = key
    return quad_and_mult(int(text), n, e)

if __name__ == '__main__':
    with open('ExampleKey.txt') as f:
        enc_key = [int(x) for x in f.read().split('\n')]
    with open('ExampleKeyDecrypt.txt') as f:
        dec_key = [int(x) for x in f.read().split('\n')]

    enc = rsa_alg(enc_key, '20')
    # print(enc)
    dec = rsa_alg(dec_key, enc)
    print(dec)