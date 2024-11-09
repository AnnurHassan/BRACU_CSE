// finding the square root of a number with a time complexity of root n.

#include <iostream>
using namespace std;

int search(int key) {

    int result = -1;
    for (int i = 1; i * i <= key; i++) {
        result = i;

    }

    return result;
}

int main() {
    cout << search(10) ;
}