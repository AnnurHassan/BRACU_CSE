#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>


int main(int argc, char *argv[]) {

    if (argc < 2) {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    int fd = open(argv[1], O_APPEND);

    printf("Enter what you want to print in the file: ");

    char input[255];
    read(STDIN_FILENO, input, sizeof(input));
    
    write(fd, input, sizeof(input));

    close(fd);
}