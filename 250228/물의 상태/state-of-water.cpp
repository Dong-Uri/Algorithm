#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int i;
    cin >> i;
    if (i < 0) cout << "ice";
    else if (i >= 100) cout << "vapor";
    else cout << "water";
    return 0;
}