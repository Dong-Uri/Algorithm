#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, B;
    cin >> A >> B;
    if (A > B) {for (A ; A >= B ; A--) cout << A << " ";}
    else {for (B ; B >= A ; B--) cout << B << " ";}
    return 0;
}