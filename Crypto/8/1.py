from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from hashlib import sha256, blake2b, md5
import base64
import random


def pad(data):
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len]) * pad_len


def unpad(data):
    return data[:-data[-1]]


def generate_rsa_keys(bits=2048):
    p = getPrime(bits // 2)
    q = getPrime(bits // 2)
    N = p * q
    e = 65537
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    return N, e, d


def encrypt_rsa(plaintext, N, e):
    message = bytes_to_long(plaintext.encode())
    return pow(message, e, N)


def xor_data(data, key):
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])


def aes_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data))
    return cipher.iv + ciphertext


def hash_mask(data, salt):
    combined = sha256(data + salt).digest()
    return xor_data(data, combined)


def multi_layer_hashing(data):
    # Multiple cryptographic hash operations for masking
    data = blake2b(data).digest()
    data = sha256(data).digest()
    return md5(data).digest()


def nested_obfuscation(data):
    for _ in range(3):  # Perform nested random operations
        op = random.choice(['base64', 'xor'])
        if op == 'base64':
            data = base64.b64encode(data)
        else:
            mask = multi_layer_hashing(data)
            data = xor_data(data, mask)
    return data


def hardened_crypto_challenge():
    # Generate RSA keys
    N, e, d = generate_rsa_keys(2048)

    # Define the flag
    flag = "flag{CTF Chakravyuha}"
    print("\n--- Hidden Challenge ---")
    print("The original flag is obfuscated through multiple cryptographic transformations.")

    # Encrypt the flag with RSA
    rsa_ciphertext = encrypt_rsa(flag, N, e)

    # XOR masking layer with dynamic random hash key
    xor_key = sha256(get_random_bytes(32)).digest()
    xor_ciphertext = rsa_ciphertext ^ int.from_bytes(xor_key, byteorder='big')

    # Base64 encode the masked ciphertext
    base64_encoded_ciphertext = base64.b64encode(str(xor_ciphertext).encode())

    # AES Encryption layer with random dynamic key
    aes_key = get_random_bytes(16)
    aes_ciphertext = aes_encrypt(base64_encoded_ciphertext, aes_key)

    # Apply nested obfuscation operations
    final_obfuscated_flag = nested_obfuscation(aes_ciphertext)

    # Final hash-based transformation layer
    encrypted_flag = hash_mask(final_obfuscated_flag, b"ai_resistant_layer")

    print("\n--- CTF Challenge Details ---")
    print(f"RSA Public Key (N, e): ({N}, {e})")
    print(f"Final Encrypted Flag (hex): {encrypted_flag.hex()}")
    print("Hint: Reverse XORs, Base64, and AES carefully.")
    print("Remember: Stealth XORs and nested operations are your keys.")


# Execute the challenge
hardened_crypto_challenge()
