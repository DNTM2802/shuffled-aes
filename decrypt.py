from SAES import saes_decrypt
import argparse
import sys

def main():
    """
    This application is used to implement the decryption of the SAES module.
    It receives two textual passwords as arguments, key and shuffle key (optional), and
    the content to be decrypted as stdin, and returns the decrypted content through stdout
    """

    # Argument parser
    parser = argparse.ArgumentParser(description='Shuffled-AES Algorithm: Decryption Application')
    parser.add_argument('key', type=str, help='decryption textual key')
    parser.add_argument('skey', type=str, nargs='?', help='shuffle textual key')
    parser.add_argument('--timeit', action='store_true', help='A boolean switch')
    args = parser.parse_args()

    # Read cipher from stdin
    cipher = sys.stdin.read()

    # Decrypt cipher text
    saes_decrypt(cipher,args.key, args.skey, timeit=args.timeit)

if __name__ == "__main__":
    main()