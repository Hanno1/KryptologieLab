import random

I = [1, 7, 11, 13, 17, 19, 23, 29]

def test_miller_rabin(n, repeat=10):
    """
    miller rabin test to test if n is a prime number. if the result is false -> n is not a prime number
    if its true -> n might be a prime number but it is not sure -> do it multiple times (repeat times)

    the algorithm is implmented as in the slides
    """
    # get k, m
    k = 1
    m = 0
    while m % 2 == 0:
        k += 1
        m = (n - 1) // 2**k

    for _ in range(repeat):
        # main algorithm for prime testing as in the slides
        a = random.randint(2, n-1)
        b = pow(a, m, n)
        if b == 1 % n:
            continue
        done = False
        for _ in range(1, k + 1):
            if b == n - 1:
                done = True
                break
            else:
                b = b**2 % n
        if done: 
            continue
        return False
    return True

def generate_prime(bits):
    """
    generate a prime number with bits length. if the number is not a prime number -> try again
    its implemented as suggested in the slides
    """
    # generate a prime number with bits length
    z = 30 * random.getrandbits(bits)
    current_i = 0
    current_index = 0
    while True:
        if test_miller_rabin(z + I[current_index] + current_i):
            return z + current_i + I[current_index]
        if current_index == len(I) - 1:
            current_i += 30
            current_index = 0
        current_index += 1

def ggt(a, b):
    """
    ggt algorithm from the slides
    """
    r = [a, b]
    s = [1, 0]
    t = [0, 1]
    while r[-1] != 0:
        q_k = r[0] // r[1]
        r.append(r[0] - q_k * r[1])
        s.append(s[0] - q_k * s[1])
        t.append(t[0] - q_k * t[1])
        r, s, t = r[1:], s[1:], t[1:]
    return r[0], s[0], t[0]

def generate_key(bits):
    """
    generate keys for the aes
    """
    # first generate 2 primes p, q that are not too close to each other
    p = generate_prime(bits)
    q = p
    while 0.66 * p < q < 1.5 * p:
        q = generate_prime(bits)

    # get phi_n
    phi_n = (p - 1) * (q - 1)
    k = 16
    # get public key e as in the slides -> starting with 2^16(=k) + 1 and incrementing k until ggt(e, phi_n) = 1
    while True:
        e = 2**k + 1
        k += 1
        if ggt(e, phi_n)[0] == 1:
            break
    # get the private key d
    d = ggt(e, phi_n)[1] % phi_n
    return (e, d, p, q)
        
if __name__ == '__main__':
    # p = generate_prime(1000)
    # q = generate_prime(1000)
    # print(p)
    print(generate_key(1000))
