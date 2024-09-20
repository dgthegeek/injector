
#include <stdio.h>

void original_function() {
    printf("I've been injected!\n");
}

int main() {
    original_function();
    return 0;
}

