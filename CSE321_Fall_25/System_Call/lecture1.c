#include <stdio.h>
// #include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>


int main() {
    
    int a = fork();

    if (a == 0) {
        
        printf("Child Process ID: %d\n", getpid());
        
        // exit(0);
    }
    else {
        
        // wait(NULL);
        printf("Parent Process ID: %d\n", getpid());
        
        // int n = wait(NULL);
        // printf("Child Process returned: %d\n", n);
        // exit(0);
    }

}