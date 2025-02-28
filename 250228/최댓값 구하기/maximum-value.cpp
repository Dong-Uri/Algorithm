#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b, c;
    cin >> a >> b >> c;
    if (a > b) {
        if (a < c) cout << c;
        else cout << a;
    }
    else {
        if (b < c) cout << c;
        else cout << b;
    }
    return 0;
}