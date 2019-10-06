from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
secret_code = "153777"
filename = "rsa_key.bin"
def make_rsa_key_to_bin_file(filename, secret_code):
    key = RSA.generate(2048)
    encrypted_key = key.export_key(passphrase=secret_code, pkcs=8, protection="scryptAndAES128-CBC")

    file_out = open(filename, "wb")
    file_out.write(encrypted_key)

    print(key.publickey().export_key())


def read_in_rsa_key_from_bin_file(filename, secret_code):
    encoded_key = open(filename, "rb").read()
    key = RSA.import_key(encoded_key, passphrase=secret_code)

    print(key.publickey().export_key())
