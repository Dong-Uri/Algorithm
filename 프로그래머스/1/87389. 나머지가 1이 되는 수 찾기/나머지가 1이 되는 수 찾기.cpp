#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    for (int m = 1 ; m < n ; m++) {
        if (n % m == 1) {answer = m; break;}
    }
    return answer;
}