#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    int i = 1;
    while (i <= N) {
        if (i % 3 == 0) cout << i << " ";
        i++;
    }
    return 0;
}