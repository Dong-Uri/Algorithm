#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    int i = 0;
    while (true) {
        i++;
        N /= i;
        if (N <= 1) break;
    }
    cout << i;
    return 0;
}