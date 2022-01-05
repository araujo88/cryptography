# Password salting example

import secrets
import string
import hashlib

PRINTABLE_CHARS = string.printable
RANDOM_STRING_CHARS = PRINTABLE_CHARS.translate(
    {ord(i): None for i in ' \t\n\r\x0b\x0c'})


def get_random_string(length, allowed_chars=RANDOM_STRING_CHARS):
    """
    Return a securely generated random string.
    The bit length of the returned value can be calculated with the formula:
        log_2(len(allowed_chars)^length)
    For example, with default `allowed_chars` (26+26+10), this gives:
      * length: 12, bit length =~ 71 bits
      * length: 22, bit length =~ 131 bits
    """
    return ''.join(secrets.choice(allowed_chars) for i in range(length))


print("Input password:")
password = input()
print("Input salt size (number of bytes):")
length = int(input())
print("Input work factor:")
work_factor = int(input())

salt = get_random_string(length)
print(f"Generated salt: {salt}")
salted_password = password + salt
print(f"Salted password: {salted_password}")
print(f"Work factor: {work_factor}")
num_iterations = 2**work_factor
print(f"Number of iterations: {num_iterations}")


for i in range(0, num_iterations):
    digest = hashlib.sha256(salted_password.encode()).hexdigest()
    salted_password = digest
    print(f"Iteration {i} - SHA-256 hash: {digest}")

print(f"Final hash: {salted_password}")
