#include <string>
#include <vector>

using namespace std;

int answer = 51;
vector<bool> visited;

void dfs(string word, string target, vector<bool>& visited, vector<string> words, int stage) {
    if (word == target) {
        if (stage < answer) answer = stage;
    }
    
    if (stage >= answer) return;
    
    for (int i = 0 ; i < words.size() ; i++) {
        if (!visited[i]) {
            int diff = 0;
            for (int j = 0 ; j < word.size() ; j++) {
                if (word[j] != words[i][j]) diff++;
            }
            if (diff == 1) {
                visited[i] = true;
                dfs(words[i], target, visited, words, stage + 1);
                visited[i] = false;
            }
        }
    }
}

int solution(string begin, string target, vector<string> words) {
    visited.assign(words.size(), false);
    dfs(begin, target, visited, words, 0);
    if (answer == 51) answer = 0;
    return answer;
}