#include <string>
#include <vector>
#include <map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    map<string, int> m;
    for (string name : participant) m[name]++;
    for (string name : completion) m[name]--;
    for (auto pair : m) {
        if (pair.second) answer = pair.first;
    }
    return answer;
}