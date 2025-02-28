#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    int s = 0;
    for (N ; N > 0 ; N--) {
        int n;
        cin >> n;
        if (n % 2 && n % 3 == 0) s += n;
    }
    cout << s;
    return 0;
}