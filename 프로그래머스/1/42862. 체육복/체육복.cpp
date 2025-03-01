#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    sort(lost.begin(), lost.end());
    sort(reserve.begin(), reserve.end());
    answer = n - lost.size();
    int i = 0, j = 0;
    while (true) {
        if (i == lost.size() || j == reserve.size()) break;
        int cha = lost[i] - reserve[j];
        if (cha < 0) i++;
        else if (cha > 0) j++;
        else {
            answer += 1;
            lost.erase(lost.begin() + i);
            reserve.erase(reserve.begin() + j);
        }
    }
    i = 0, j = 0;
    while (true) {
        if (i == lost.size() || j == reserve.size()) break;
        int cha = lost[i] - reserve[j];
        if (cha < -1) i++;
        else if (cha > 1) j++;
        else {
            answer += 1;
            i++;
            j++;
        }
    }
    return answer;
}