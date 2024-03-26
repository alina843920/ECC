from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.padding import PKCS7

private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
public_key = private_key.public_key()

message = input("wiadomość: ")
message = message.encode() 

shared_key = private_key.exchange(ec.ECDH(), public_key)

cipher = Cipher(algorithms.AES(shared_key), modes.ECB(), backend=default_backend())
encryptor = cipher.encryptor()

padder = PKCS7(128).padder()
padded_data = padder.update(message) + padder.finalize()

ciphertext = encryptor.update(padded_data) + encryptor.finalize()

print("zaszyfrowana:", ciphertext)

cipher = Cipher(algorithms.AES(shared_key), modes.ECB(), backend=default_backend())
decryptor = cipher.decryptor()

unpadder = PKCS7(128).unpadder()
plaintext = unpadder.update(decryptor.update(ciphertext) + decryptor.finalize()) + unpadder.finalize()

print("odszyfrowana:", plaintext.decode())
