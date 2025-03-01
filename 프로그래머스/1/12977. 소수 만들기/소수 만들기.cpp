#include <vector>
#include <iostream>
using namespace std;

int solution(vector<int> nums) {
    int answer = 0;
    for (int i = 0 ; i < nums.size() - 2 ; i++) {
        for (int j = i + 1 ; j < nums.size() - 1 ; j++) {
            for (int k = j + 1 ; k < nums.size() ; k++) {
                int num = nums[i] + nums[j] + nums[k];
                bool is_prime = true;
                for (int n = 2 ; n < num ; n++) {
                    if (num % n == 0) {
                        is_prime = false;
                        break;
                    }
                }
                if (is_prime) answer++;
            }
        }
    }
    return answer;
}