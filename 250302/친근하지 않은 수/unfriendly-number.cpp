#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    int cnt = 0;
    for (N ; N > 0 ; N--) {
        if (N % 2 && N % 3 && N % 5) cnt++;
    }
    cout << cnt;
    return 0;
}