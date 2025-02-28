#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A1, A2, B1, B2;
    cin >> A1 >> A2 >> B1 >> B2;
    if (A1 > B1) cout << 'A';
    else if (A1 < B1) cout << 'B';
    else {
        if (A2 > B2) cout << 'A';
        else if (A2 < B2) cout << 'B';
    }
    return 0;
}