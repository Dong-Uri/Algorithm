#include <string>
#include <vector>

using namespace std;

int answer = 0;
int hap, target_sum;

void dfs(int i, int sum, int target_sum, vector<int> numbers) {
    if (sum == target_sum) {
        answer++;
        return;
    }
    if (i == numbers.size() || sum > target_sum) return;
    dfs(i + 1, sum, target_sum, numbers);
    dfs(i + 1, sum + numbers[i], target_sum, numbers);
    
}

int solution(vector<int> numbers, int target) {
    for (int n : numbers) hap += n;
    if ((hap + target) % 2) return 0;
    target_sum = (hap - target) / 2;
    dfs(0, 0, target_sum, numbers);
    return answer;
}