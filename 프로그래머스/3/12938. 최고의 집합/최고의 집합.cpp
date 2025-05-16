#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, int s) {
    vector<int> answer;
    if (n > s) answer.push_back(-1);
    else {
        answer.assign(n, s / n);
        for (int i = 0; i < s % n; i++) answer[n - 1 - i]++;
    }
    return answer;
}