#include <string>
#include <vector>

using namespace std;

string solution(vector<int> numbers, string hand) {
    string answer = "";
    pair<int, int> num_index[10] = {{2, 4}, {1, 1}, {2, 1}, {3, 1}, {1, 2}, {2, 2}, {3, 2}, {1, 3}, {2, 3}, {3, 3}};
    pair<int, int> left = {1, 4};
    pair<int, int> right = {3, 4};
    for (int num : numbers) {
        if (num == 1 || num == 4 || num == 7) {
            left = num_index[num];
            answer += 'L';
        }
        else if (num == 3 || num == 6 || num == 9) {
            right = num_index[num];
            answer += 'R';
        }
        else {
            int left_far = abs(left.first - num_index[num].first) + abs(left.second - num_index[num].second);
            int right_far = abs(right.first - num_index[num].first) + abs(right.second - num_index[num].second);
            if (left_far < right_far) {
                left = num_index[num];
                answer += 'L';
            }
            else if (left_far > right_far) {
                right = num_index[num];
                answer += 'R';
            }
            else {
                if (hand == "left") {
                    left = num_index[num];
                    answer += 'L';
                }
                if (hand == "right") {
                    right = num_index[num];
                    answer += 'R';
                }
            }
        }
    }
    return answer;
}