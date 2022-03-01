from SAES import saes_encrypt
import argparse
import sys

def main():
    """
    This application is used to implement the encryption of the SAES module.
    It receives two textual passwords as arguments, key and shuffle key (optional), and
    the content to be encrypted as stdin, and returns the encrypted content through stdout
    """

    # Argument parser
    parser = argparse.ArgumentParser(description='Shuffled-AES Algorithm: Encryption Application')
    parser.add_argument('key', type=str, help='encryption textual key')
    parser.add_argument('skey', type=str, nargs='?', help='shuffle textual key')
    parser.add_argument('--timeit', action='store_true', help='A boolean switch')
    args = parser.parse_args()

    # Read plain from stdin
    plain = sys.stdin.read()

    # Encrypt plain text
    saes_encrypt(plain,args.key,args.skey, timeit=args.timeit)

if __name__ == "__main__":
    main()