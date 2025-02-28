#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A;
    cin >> A;
    if (A % 3 == 0) cout << "YES";
    else cout << "NO";
    cout << endl;
    if (A % 5 == 0) cout << "YES";
    else cout << "NO";
    return 0;
}