#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    int s = 0;
    for (N ; N <= 100 ; N++) s += N;
    cout << s;
    return 0;
}