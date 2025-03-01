#include <string>
#include <vector>

using namespace std;

long long solution(int a, int b) {
    long long answer = 0;
    if (a < b) {
        answer = (b - a + 1) * (long long)(b + a);
    }
    else {
        answer = (a - b + 1) * (long long)(b + a);
    }
    answer /= 2;
    return answer;
}