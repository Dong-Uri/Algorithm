#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    int sum = 0;
    int ans;
    for (int i = 1 ; i <= 100 ; i++) {
        sum += i;
        ans = i;
        if (sum >= N) break;
    }
    cout << ans;
    return 0;
}