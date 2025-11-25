#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

// Function to safely read a long integer from stdin
int read_long(long *num) {
    char buffer[100];
    if (fgets(buffer, sizeof(buffer), stdin) == NULL) {
        return 0; // Input error
    }

    char *endptr;
    *num = strtol(buffer, &endptr, 10);

    // Check for conversion errors
    if (endptr == buffer || *endptr != '\n') {
        return 0; // Not a valid integer
    }
    return 1; // Success
}

int main() {
    long a, b, c;

    printf("Enter first number: ");
    if (!read_long(&a)) {
        printf("Invalid input. Please enter a valid integer.\n");
        return 1;
    }

    printf("Enter second number: ");
    if (!read_long(&b)) {
        printf("Invalid input. Please enter a valid integer.\n");
        return 1;
    }

    printf("Enter third number: ");
    if (!read_long(&c)) {
        printf("Invalid input. Please enter a valid integer.\n");
        return 1;
    }

    // Compare the numbers
    if (a == b && b == c) {
        printf("All three numbers are equal.\n");
    } 
    else if (a != b && b != c && a != c) {
        printf("All three numbers are different.\n");
    } 
    else {
        printf("Some numbers are equal, but not all.\n");
    }

    // Find the largest number
    long largest = a;
    if (b > largest) largest = b;
    if (c > largest) largest = c;

    printf("The largest number is: %ld\n", largest);

    return 0;
}
