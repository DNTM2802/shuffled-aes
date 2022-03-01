from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import sys
import binascii
import hashlib
import time
import argparse
import sys

def main():
    """
    This application is used to implement and test the performance of the
    encryption/decrytion modules of the Cryptography library. It receives
    a textual password and data from the stdin, and writes the encryption
    and decryption times to the folder .times.
    """

    # Argument parser
    parser = argparse.ArgumentParser(
        description='Python Cryptography AES Algorithm: Encryption/Descryption performance testing application')
    parser.add_argument('key', type=str, help='encryption textual key')
    args = parser.parse_args()

    # Read plain from stdin
    plain = sys.stdin.read()

    # Initialize key
    key = hashlib.md5(bytes(args.key, encoding='utf8')).digest()

    # Initialize cipher
    cipher = Cipher(algorithms.AES(key), modes.ECB(),backend=default_backend())
    
    # Initialize encryptor
    encryptor = cipher.encryptor()

    start = time.time_ns()

    # Perform encryption
    ct = encryptor.update(bytes(plain,"ascii")) + encryptor.finalize()

    end = time.time_ns()

    time_file_enc = open(f'times/aes-crypto_encrypt_times.txt', 'a')
    overall = (end - start) / (10 ** 9)
    time_file_enc.write(str('{:0.9f}\n'.format(overall)))

    # Initialize decryptor
    decryptor = cipher.decryptor()

    start = time.time_ns()

    # Perform decryption
    plain_decrypted = decryptor.update(ct) + decryptor.finalize()

    end = time.time_ns()

    time_file_dec = open(f'times/aes-crypto_decrypt_times.txt', 'a')
    overall = (end - start) / (10 ** 9)
    time_file_dec.write(str('{:0.9f}\n'.format(overall)))


if __name__ == "__main__":
    main()