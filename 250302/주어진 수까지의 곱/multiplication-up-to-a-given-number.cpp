#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, B;
    cin >> A >> B;
    int ans = 1;
    for (A ; A <= B ; A++) ans *= A;
    cout << ans;
    return 0;
}