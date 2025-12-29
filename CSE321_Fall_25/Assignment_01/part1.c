#include <stdio.h>  
#include <unistd.h>    // needed for fork()
#include <stdlib.h>    // needed for exit() call 
#include <sys/wait.h>  // needed for wait() call


int main() {
    
    int a = fork();                                    // create a child process

    if (a == 0) {                                      // for child process
         
        printf("Child Process ID: %d\n", getpid());    // print the child Process ID
        
        // exit(0);                                    // Not necessary for this instant but can be used to exit a process 
    }
    else {                                             // for parent process
        
        wait(NULL);                                    // wait for the child process to finish first (if no wait child will be a zombie process)
        printf("Parent Process ID: %d\n", getpid());   // print the parent process ID
        
        // int n = wait(NULL);                         // wait also returns the process ID of child process
        // printf("Child Process returned: %d\n", n);
        
        // exit(0);
    }

}