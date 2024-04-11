#include <stdio.h>
#include <unistd.h>

int main() {
    printf("start!\n");
    int forkRet = fork();
    if (forkRet == 0) {
        printf("child process %d\n", getpid());
    } else {
        printf("forkRet:%d parent process:%d\n", forkRet, getpid());
    }
    return 0;
}