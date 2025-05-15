#include <iostream>
#include <vector>

using namespace std;

void dfs(int node, vector<vector<int>>& computers, vector<bool>& visited) {
    visited[node] = true;
    
    for (int next = 0; next < computers.size(); next++) {
        if (computers[node][next] == 1 && !visited[next]) {
            dfs(next, computers, visited);
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    vector<bool> visited(n, false);

    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            answer++;  // 새로운 네트워크 발견
            dfs(i, computers, visited);
        }
    }

    return answer;
}