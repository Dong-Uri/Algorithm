#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, B;
    cin >> A >> B;
    int s = 0;
    for (A ; A <= B ; A++) {
        s += A;
    }
    cout << s;
    return 0;
}