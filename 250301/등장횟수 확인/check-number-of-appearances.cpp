#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int cnt = 0;
    for (int i = 5 ; i > 0 ; i--) {
        int n;
        cin >> n;
        if (n % 2 == 0) cnt++;
    }
    cout << cnt;
    return 0;
}