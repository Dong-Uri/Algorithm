#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    int s = 0;
    for (int i = 1 ; i <= N / 2 ; i++) {
        if (N % i == 0) s += i;
    }
    if (s == N) cout << 'P';
    else cout << 'N';
    return 0;
}