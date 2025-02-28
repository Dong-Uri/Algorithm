#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b, c;
    cin >> a >> b >> c;
    if (a <= b && b <= c) cout << a;
    else if (b <= c) cout << b;
    else cout << c;
    return 0;
}