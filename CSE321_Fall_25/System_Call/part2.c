#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {

    printf("File: Part2 Executing........\n");

    int a = fork();

    if (a == 0) {
        
        printf("File: Part1 Executing......\n");
        char *agrv[] = {"./1", NULL};
        execv(agrv[0], agrv); 
        // execl("./1", "./1", NULL); 
    }
    else {
        wait(NULL);
        printf("File: Part1 Complete.\n");
        printf("File: Part2 Complete.\n");

    }


}