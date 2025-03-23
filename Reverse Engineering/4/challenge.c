#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdint.h>
#include <unistd.h>
#include <sys/ptrace.h>
#include <openssl/sha.h>
#include <openssl/aes.h>

#define OBFUSCATE(x) ((x) ^ 0xDEADBEEF)

// Anti-debugging mechanism
void anti_debug() {
    if (ptrace(PTRACE_TRACEME, 0, 1, 0) == -1) {
        printf("Debugger detected!\n");
        exit(1);
    }
}

// Opaque predicate
int opaque_predicate(int x) {
    return ((x * x + 1) % 3 == 1);
}

// Custom XOR encryption
void xor_encrypt(char *data, size_t len, char key) {
    for (size_t i = 0; i < len; i++) {
        data[i] ^= key;
    }
}

// Self-modifying code
void self_modify() {
    unsigned char *ptr = (unsigned char *)&self_modify;
    for (int i = 0; i < 20; i++) {
        ptr[i] ^= (i * 7 + 3);
    }
}

// Dynamic flag generation
void generate_flag(const char *password, char *flag) {
    sprintf(flag, "G8KEY{1865A512}");
}

int main() {
    anti_debug();
    self_modify();

    char input[64];
    char flag[64];
    const char *correct_password = "\x18\x13\x12\x78\x53\x16\x12\x13\x12\x5F\x5C\x1D\x08\x0F"; // XOR encrypted with key 0x3C
    char key = 0x3C;

    printf("Enter the password: ");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = 0; // Remove newline

    xor_encrypt(input, strlen(input), key);

    if (opaque_predicate(time(NULL))) {
        if (memcmp(input, correct_password, 14) == 0) {
            generate_flag(input, flag);
            printf("Correct! Here is your flag: %s\n", flag);
        } else {
            printf("Incorrect password!\n");
        }
    } else {
        printf("Unexpected error.\n");
    }

    return 0;
}
