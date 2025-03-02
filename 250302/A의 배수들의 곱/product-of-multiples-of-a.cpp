#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, B;
    cin >> A >> B;
    int ans = 1;
    for (B ; B > 0 ; B--) {
        if (B % A == 0) ans *= B;
    }
    cout << ans;
    return 0;
}