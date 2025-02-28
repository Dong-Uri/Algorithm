#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, B;
    cin >> A >> B;
    int s = 0;
    if (A < B) for (A ; A <= B ; A++) {
        if (A % 5 == 0) s += A;
    }
    else for (A ; A >= B ; A--) {
        if (A % 5 == 0) s += A;
    }
    cout << s;
    return 0;
}