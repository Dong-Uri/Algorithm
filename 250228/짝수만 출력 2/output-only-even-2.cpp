#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, B;
    cin >> B >>A ;
    while (B >= A) {
        cout << B << " ";
        B -= 2;
    }
    return 0;
}