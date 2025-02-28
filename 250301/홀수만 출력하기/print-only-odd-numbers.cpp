#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    for (N ; N > 0 ; N --) {
        int n;
        cin >> n;
        if (n % 2 && n % 3 == 0) cout << n << endl;
    }
    return 0;
}