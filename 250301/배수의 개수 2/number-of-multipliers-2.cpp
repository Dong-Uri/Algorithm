#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int cnt = 0;
    for (int i = 10 ; i > 0 ; i--) {
        int n;
        cin >> n;
        if (n % 2) cnt++;
    }
    cout << cnt;
    return 0;
}