#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for (vector<int> c : commands) {
        vector<int> sub_array(array.begin() + c[0] - 1, array.begin() + c[1]);
        sort(sub_array.begin(), sub_array.end());
        answer.push_back(sub_array[c[2] - 1]);
        
    }
    return answer;
}