#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, B;
    cin >> A >> B;
    cout << A / B;
    A %= B;
    cout << '.';
    for (int i = 20 ; i > 0 ; i--) {
        A *= 10;
        cout << A / B;
        A %= B;
    }
    return 0;
}