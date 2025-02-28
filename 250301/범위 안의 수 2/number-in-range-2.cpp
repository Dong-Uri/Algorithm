#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int c = 0;
    int s = 0;
    for (int i = 10 ; i > 0 ; i--) {
        int n;
        cin >> n;
        if (n >= 0 && n <= 200) {
            c++;
            s += n;
        }
    }
    cout << fixed;
    cout.precision(1);
    cout << s << " " << (double)s/c;
    return 0;
}