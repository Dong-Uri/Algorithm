#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, B, C;
    cin >> A >> B >> C;
    if (A > B) {
        if (C > A) cout << A;
        else if (B > C) cout << B;
        else cout << C;
    }
    else {
        if (C > B) cout << B;
        else if (A > C) cout << A;
        else cout << C;
    }
    return 0;
}