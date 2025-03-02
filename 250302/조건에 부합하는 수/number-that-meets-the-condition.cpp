#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A;
    cin >> A;
    for (int a = 1 ; a <= A ; a++) {
        if (a % 2 == 0 && a % 4) continue;
        if ((a / 8) % 2 == 0) continue;
        if (a % 7 < 4) continue;
        cout << a << " ";
    }
    return 0;
}