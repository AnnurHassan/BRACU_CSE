#include <iostream>
using namespace std;

int search(int key) {

    if (key < 0) {       
        return -1;
    }

    if (key == 0 || key == 1) {      
        return key;
    }

    int l = 0;
    int r = key;
    int result = 0;

    while (l <= r) {

        int mid = (l + r) / 2;

        if (mid * mid == key) {
            return mid;
        }

        else if (mid * mid < key) {       
            l += 1;
            result = mid;
        }

        else {
            r -= 1;
        }
    }

    return result;


}

int main() {

    int key = 0;
    cout << "Enter the Key: ";
    cin >> key;
    cout << search(key) ;

}