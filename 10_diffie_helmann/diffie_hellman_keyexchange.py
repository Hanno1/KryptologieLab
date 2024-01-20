import random

I = [1, 7, 11, 13, 17, 19, 23, 29]

def test_miller_rabin(n, repeat=10):
    """
    miller rabin prime test repeated repeat times for the number n. Its repeated to get a higher probability of correctness
    its implemented as written on the slides
    """
    k = 1
    m = n - 1
    while m % 2 == 0:
        m //= 2
        k += 1
    for _ in range(repeat):
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
    generate a prime number with bits length using the algorithms given on the slide and test for primality with miller rabin
    """
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

def get_generator(bits = 1000):
    """
    get the generator number g and a prime number p with bits length
    """
    # search for q prim, that p = 2*q + 1 is prim
    q = generate_prime(bits)
    p = 2 * q + 1
    while not test_miller_rabin(p):
        q = generate_prime(bits)
        p = 2 * q + 1
    # get random g between 2 and p-2
    g = random.randint(2, p - 2)
    return p, g

def get_result(bits):
    """
    computes all needed values for this task. p is the prime number, g is the generator, 
    A is the result of Allice and B is the result of Bob. S is the shared key and therefore the key that can be used for AES

    variablenames correspond to names in the slides
    """
    p, g = get_generator(bits)
    a = random.randint(2, p - 2)
    b = random.randint(2, p - 2)
    A = pow(g, a, p)
    B = pow(g, b, p)
    s1 = pow(B, a, p)
    s2 = pow(A, b, p)
    return s1, s2, p, g, A, B

if __name__ == '__main__':
    print(get_result(100))
    # print(test_miller_rabin(40203))
