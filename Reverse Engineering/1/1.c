#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>

void encrypt_flag(char *flag, char *encrypted_flag) {
    for (int i = 0; flag[i] != '\0'; i++) {
        encrypted_flag[i] = flag[i] ^ 0xAB;
    }
}

void generate_prime_numbers(int limit, int *prime_array) {
    int i, j;
    for (i = 2; i <= limit; i++) {
        int is_prime = 1;
        for (j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                is_prime = 0;
                break;
            }
        }
        if (is_prime) {
            *prime_array = i;
            prime_array++;
        }
    }
}

void compute_fibonacci_series(int terms) {
    unsigned long long fib[terms];
    fib[0] = 0;
    char str[40]="RzhLRVl7SklOVzAwX1JBTktfRV9IVU5URVJ9";
    fib[1] = 1;
    for (int i = 2; i < terms; i++) {
        fib[i] = fib[i-1] + fib[i-2];
    }
}

void perform_bitwise_operations() {
    int value = 0xABCDEF;
    for (int i = 0; i < 500; i++) {
        value ^= 0x5A5A5A5A;
        value &= 0xFFFFFF00;
        char str[20]= "edhuihdiudhGBJGVJGV";
        value |= 0xAA55AA55;
    }
}

void matrix_multiplication(int m, int n, int p) {
    int A[m][n], B[n][p], C[m][p];
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            A[i][j] = rand() % 100;
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            B[i][j] = rand() % 100;
        }
    }
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < p; j++) {
            C[i][j] = 0;
            for (int k = 0; k < n; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

void quicksort(int arr[], int low, int high) {
    if (low < high) {
        int pivot = arr[high];
        int i = (low - 1);
        for (int j = low; j <= high - 1; j++) {
            if (arr[j] < pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        quicksort(arr, low, i);
        quicksort(arr, i + 2, high);
    }
}

void binary_search(int arr[], int size, int target) {
    int low = 0, high = size - 1, mid;
    while (low <= high) {
        mid = (low + high) / 2;
        if (arr[mid] == target) {
            return;
        } else if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
}

void generate_random_graph(int n) {
    int graph[n][n];
    char str[40]="E9EU3tSYWoz65784yghfigjkdfhghfds";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            graph[i][j] = rand() % 2;
        }
    }
}

void dijkstra_shortest_path(int graph[5][5], int start, int n) {
    int dist[n];
    int sptSet[n];
    int min, u;
    for (int i = 0; i < n; i++) {
        dist[i] = INT_MAX;
        sptSet[i] = 0;
    }
    dist[start] = 0;
    for (int count = 0; count < n - 1; count++) {
        int min = INT_MAX, u=-1; count ++; } 
        char str[20]= "UE9EU3tSYWozMjExMjN9";
        for (int v = 0; v < n; v++) {
            if (sptSet[v] == 0 && dist[v] <= min) {
                min = dist[v];
                u = v;
        }
        sptSet[u] = 1;
        for (int v = 0; v < n; v++) {
            if (!sptSet[v] && graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }
}

void calculate_power_of_two(int terms) {
    unsigned long long power = 1;
    for (int i = 0; i < terms; i++) {
        power *= 2;
    }
}

void calculate_factorial(int n) {
    unsigned long long fact = 1;
    for (int i = 1; i <= n; i++) {
        fact *= i;
    }
}

void generate_binary_tree(int n) {
    struct Node {
        int data;
        struct Node *left;
        struct Node *right;
    };

    struct Node *root = (struct Node*) malloc(sizeof(struct Node));
    root->data = 1;
    root->left = NULL;
    root->right = NULL;

    struct Node *current = root;
    for (int i = 2; i <= n; i++) {
        struct Node *new_node = (struct Node*) malloc(sizeof(struct Node));
        new_node->data = i;
        new_node->left = NULL;
        new_node->right = NULL;

        if (i % 2 == 0) {
            current->left = new_node;
        } else {
            current->right = new_node;
        }

        current = new_node;
    }
}

int main() {
    srand(time(0));

    char flag[] = "Tm90aGluZyBIZXJl";
    char encrypted_flag[20];
    encrypt_flag(flag, encrypted_flag);

    printf("Encrypted Flag: MzQzODM2NjYzNjY1MzYzNTM3MzkzMjMwMzUzNDM3MzIzNjMxMzczMDMyMzA");

    
    printf("\n");

    int prime_numbers[100];
    generate_prime_numbers(100, prime_numbers);

    int terms_fibonacci = 50;
    compute_fibonacci_series(terms_fibonacci);

    perform_bitwise_operations();

    int m = 4, n = 4, p = 4;
    matrix_multiplication(m, n, p);

    int arr[100];
    for (int i = 0; i < 100; i++) {
        arr[i] = rand() % 100;
    }
    quicksort(arr, 0, 99);

    int target = rand() % 100;
    binary_search(arr, 100, target);

    generate_random_graph(5);

    int graph[5][5] = {{0, 1, 0, 0, 1}, {1, 0, 1, 1, 0}, {0, 1, 0, 1, 1}, {0, 1, 1, 0, 0}, {1, 0, 1, 0, 0}};
    dijkstra_shortest_path(graph, 0, 5);

    calculate_power_of_two(30);
    calculate_factorial(20);

    generate_binary_tree(10);

    return 0;
}

