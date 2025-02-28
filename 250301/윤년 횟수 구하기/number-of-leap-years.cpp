#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int cnt = 0;
    int N;
    cin >> N;
    for (int i = 1 ; i <= N ; i++) {
        if (i % 4 == 0) cnt++;
        if (i % 100 == 0 && i % 400 != 0) cnt--;
    }
    cout << cnt;
    return 0;
}