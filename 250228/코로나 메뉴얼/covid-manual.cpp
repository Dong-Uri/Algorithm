#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    char aa, bb, cc;
    int a, b, c;
    cin >> aa >> a >> bb >> b >> cc >> c;
    int x = 0;
    if (aa == 'Y' && a >= 37) x += 1;
    if (bb == 'Y' && b >= 37) x += 1;
    if (cc == 'Y' && c >= 37) x += 1;
    if (x >= 2) cout << 'E';
    else cout << 'N';
    return 0;
}