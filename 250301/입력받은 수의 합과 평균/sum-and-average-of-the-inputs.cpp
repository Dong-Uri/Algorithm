#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    int s = 0;
    for (int i = 1 ; i <= N ; i++) {
        int n;
        cin >> n;
        s += n;
    }
    cout << fixed;
    cout.precision(1);
    cout << s << " " << (double)s/N;
    return 0;
}