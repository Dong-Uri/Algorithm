#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int M;
    cin >> M;
    if (M <= 2) cout << "Winter";
    else if (M <= 5) cout << "Spring";
    else if (M <= 8) cout << "Summer";
    else if (M <= 11) cout << "Fall";
    else cout << "Winter";
    return 0;
}