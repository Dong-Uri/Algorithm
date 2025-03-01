#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    int a = 0, b = 0, c = 0;
    int x = 0, y = 0, z = 0;
    int A[5] = {1, 2, 3, 4, 5};
    int B[8] = {2, 1, 2, 3, 2, 4, 2, 5};
    int C[10] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    for (int i = 0 ; i < answers.size() ; i++) {
        if (answers[i] == A[a]) x++;
        if (answers[i] == B[b]) y++;
        if (answers[i] == C[c]) z++;
        a++, b++, c++;
        if (a == 5) a = 0;
        if (b == 8) b = 0;
        if (c == 10) c = 0;
    }
    if (x >= y && x >= z) answer.push_back(1);
    if (y >= x && y >= z) answer.push_back(2);
    if (z >= x && z >= y) answer.push_back(3);
    return answer;
}