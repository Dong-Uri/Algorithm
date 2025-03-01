#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    vector<int> basket;
    for (int m : moves) {
        for (int i = 0; i < board.size() ; i++) {
            if (board[i][m-1]) {
                if (basket.empty()) {
                    basket.push_back(board[i][m-1]);
                } else if(basket.back() == board[i][m-1]) {
                    basket.pop_back();
                    answer += 2;
                } else {
                    basket.push_back(board[i][m-1]);
                }
                board[i][m-1] = 0;
                break;
            }
        }
    }
    return answer;
}