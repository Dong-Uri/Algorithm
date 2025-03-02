#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    for (int n = 1 ; n <= N ; n++) {
        if (n % 2 == 0) continue;
        if (n % 10 == 5) continue;
        if (n % 3 == 0 && n % 9) continue;
        cout << n << " ";
    }
    return 0;
}