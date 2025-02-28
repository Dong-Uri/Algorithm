#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, B;
    cin >> A >> B;
    while (A <= B) {
        cout << A << " ";
        if (A % 2) A *= 2;
        else A += 3;
    }
    return 0;
}