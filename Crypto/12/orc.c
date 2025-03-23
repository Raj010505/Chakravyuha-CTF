#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/evp.h>
#include <openssl/rand.h>

#define FLAG "G8KEY{H1GH_0RC_DUNG30N_R@1D}"
#define KEY_SIZE 32
#define BLOCK_SIZE 16
#define MUTATION_ROUNDS 5
#define OBFUSCATION_LAYERS 3

void handle_errors() {
    fprintf(stderr, "An error occurred.\n");
    exit(EXIT_FAILURE);
}

void generate_random_bytes(unsigned char *buffer, int length) {
    if (!RAND_bytes(buffer, length)) handle_errors();
}

void key_mutation(unsigned char *key, size_t key_len) {
    for (int round = 0; round < MUTATION_ROUNDS; round++) {
        for (size_t i = 0; i < key_len; i++) {
            key[i] ^= (key[(i + 1) % key_len] + round) % 256;
            key[i] = (key[i] << 1) | (key[i] >> 7); // Bit rotation
        }
    }
}

void nonlinear_transform(unsigned char *data, size_t len) {
    for (size_t i = 0; i < len; i++) {
        data[i] = ((data[i] * 37) ^ (data[(i + 7) % len] * 13)) % 256;
    }
}

void encrypt(unsigned char *plaintext, int plaintext_len, unsigned char *key, unsigned char *ciphertext) {
    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
    if (!ctx) handle_errors();

    unsigned char iv[BLOCK_SIZE];
    generate_random_bytes(iv, BLOCK_SIZE);

    if (EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv) != 1) handle_errors();

    int len;
    if (EVP_EncryptUpdate(ctx, ciphertext, &len, plaintext, plaintext_len) != 1) handle_errors();
    int ciphertext_len = len;

    if (EVP_EncryptFinal_ex(ctx, ciphertext + len, &len) != 1) handle_errors();
    ciphertext_len += len;

    EVP_CIPHER_CTX_free(ctx);
}

int main() {
    unsigned char key[KEY_SIZE];
    generate_random_bytes(key, KEY_SIZE);
    key_mutation(key, KEY_SIZE);

    unsigned char plaintext[] = FLAG;
    size_t plaintext_len = strlen(FLAG);

    unsigned char ciphertext[1024];

    for (int i = 0; i < OBFUSCATION_LAYERS; i++) {
        nonlinear_transform(plaintext, plaintext_len);
    }

    encrypt(plaintext, plaintext_len, key, ciphertext);

    printf("Encrypted ciphertext: \n");
    for (size_t i = 0; i < plaintext_len + BLOCK_SIZE; i++) {
        printf("%02x", ciphertext[i]);
    }
    printf("\n");

    return 0;
}
