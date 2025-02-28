#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    for (int i = 1 ; i <= N ; i++) {
        cout << (i % 2 == 0 || i % 3 == 0) << " ";
    }
    return 0;
}