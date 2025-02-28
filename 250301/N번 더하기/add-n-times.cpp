#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, N;
    cin >> A >> N;
    for (int i = N; i > 0 ; i--) {
        A += N;
        cout << A << endl;
    }
    return 0;
}