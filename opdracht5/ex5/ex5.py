"""
Auteur: Mark Jansen
Studentnummer: 13385569
Gemaakt op: 7-12-2022

Samenvatting:
Dit programma kraakt een RSA encryptie door middel van
het achterhalen van de factoren en multiplicative inverse
te berekenen.

Gebruik:
- Run de de python code met python3 <pythonfile> <inputfile>
- Het resultaat wordt naar standard output gestuurd.
"""

import fileinput
import math


def first_factor(n):
    """
    Calculate the first factor of product

    n = int, which holds the product of primes

    Output: The first factor.
    """
    f = math.floor(math.sqrt(n))
    while (n % f != 0):
        f -= 1
    return f


def crack(n, pb_key, enc_msg):
    """
    Crack the message by figuring out the factors and
    the multiplicative inverse of the public key.

    n = int, which holds product of primes
    pb_key = int, which holds the public key
    enc_msg = int, which holds the message to be decrypted.

    Side-effect: Print answer to standard output.
    """
    p = first_factor(n)  # First factor
    q = int(n / p)  # Second factor
    t = (p - 1) * (q - 1)  # Euler's toitient
    d = pow(pb_key, -1, t)  # Decryption key

    print(pow(enc_msg, d, n))  # Decryption


if __name__ == "__main__":
    for line in fileinput.input():
        if not fileinput.isfirstline():
            line = list(map(int, line.split(" ")))
            crack(line[0], line[1], line[2])
