#include <stdio.h>

int main() {
    int num;

    // Ask the user for a number
    printf("Enter an integer: ");
    scanf("%d", &num);

    // Check if the number is even
    if (num % 2 == 0) {
        printf("%d is even.\n", num);
    } else {
        printf("%d is odd.\n", num);
    }

    return 0;
}
https://youtu.be/6WXVkGX4K24?si=9nJ4ol5F1GnIsG6m
