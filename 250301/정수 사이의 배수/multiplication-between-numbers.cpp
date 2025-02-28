#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, B;
    cin >> A >> B;
    int c = 0;
    int s = 0;
    for (A ; A <= B ; A++) {
        if (A % 5 == 0 or A % 7 == 0){
            c++;
            s += A;
        }
    }
    cout << fixed;
    cout.precision(1);
    cout << s << " " << (double)s/c;
    return 0;
}