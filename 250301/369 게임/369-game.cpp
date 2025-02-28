#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    for (int i = 1 ; i <= N ; i++) {
        if (i % 3 == 0 || i % 10 == 3 || (i / 10) % 10 == 3) cout << 0 << " ";
        else cout << i << " ";
    }
    return 0;
}