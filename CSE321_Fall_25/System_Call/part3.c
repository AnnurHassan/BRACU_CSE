#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>


int main() {

    int fd = open("input.txt", O_WRONLY | O_APPEND);
    char buffer[100];

    int bytes = read(fd, buffer, sizeof(buffer));

    printf("%s\n", buffer);
    // write(STDOUT_FILENO, buffer, bytes);

    char text[] = "Hello World from Write\n";

    write(fd, text, sizeof(text));

     close(fd);

}