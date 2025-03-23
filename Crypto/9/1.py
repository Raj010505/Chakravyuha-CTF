from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from hashlib import sha256, blake2b, md5
import base64
import random


def xor_bytes(data, key):
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])


def multi_layer_hash(data):
    # Multi-step cryptographic hash transformation
    hashed = sha256(data).digest()
    hashed = blake2b(hashed).digest()
    return md5(hashed).digest()


def nested_encoding(data):
    # Randomly apply base64 encoding and XOR transformations
    for _ in range(5):  # Increase nested complexity
        operation = random.choice(["base64", "xor"])
        if operation == "base64":
            data = base64.b64encode(data)
        else:
            mask = multi_layer_hash(data)
            data = xor_bytes(data, mask)
    return data


def encrypt_aes(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))
    return cipher.iv + ciphertext


def decrypt_aes(ciphertext, key):
    iv = ciphertext[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext[16:]))


def generate_rsa_keys():
    # Generate a secure RSA key pair
    key = RSA.generate(2048)
    public_key = key.publickey()
    return key, public_key


def encrypt_rsa(data, public_key):
    # Encrypt data using RSA and PKCS1_OAEP padding
    cipher = PKCS1_OAEP.new(public_key)
    return cipher.encrypt(data)


def hardened_crypto_challenge():
    # Define the flag
    flag = "flag{cipher_cascade}"

    print("\n--- Cipher Cascade Challenge ---")
    print("This challenge involves multiple cryptographic layers and obfuscation techniques.")

    # Step 1: AES Encryption with a random key

    aes_key = get_random_bytes(16)
    cipher_aes = AES.new(aes_key, AES.MODE_CBC)
    iv = cipher_aes.iv
    ciphertext_aes = cipher_aes.encrypt(pad(flag.encode(), AES.block_size))

    # Step 2: Generate RSA Key Pair

    rsa_key, public_key = generate_rsa_keys()

    # Step 3: Encrypt AES key using RSA

    encrypted_aes_key = encrypt_rsa(aes_key, public_key)

    # Step 4: XOR obfuscation layer for AES ciphertext

    xor_mask = sha256(get_random_bytes(32)).digest()
    xor_ciphertext = xor_bytes(ciphertext_aes, xor_mask)

    # Step 5: Base64 encode the XOR-obfuscated AES ciphertext

    encoded_ciphertext = base64.b64encode(xor_ciphertext)

    # Step 6: Nested obfuscation operations

    nested_encoded_flag = nested_encoding(encoded_ciphertext)

    # Step 7: Final cryptographic hash-based masking

    final_encrypted_data = multi_layer_hash(nested_encoded_flag)

    # Display challenge details

    print("\n--- Challenge Details ---")
    print(f"RSA Public Key (n, e): ({public_key.n}, {public_key.e})")
    print(f"RSA Encrypted AES Key (hex): {encrypted_aes_key.hex()}")
    print(f"Final Encrypted Data (hex): {final_encrypted_data.hex()}")
    print("Hint: Carefully reverse obfuscation layers involving XOR, Base64, and nested transformations.")
    print("Remember: Hash masks and nested encodings are key elements.")


# Execute the hardened crypto challenge

hardened_crypto_challenge()
