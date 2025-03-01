#include <string>
#include <vector>

#include<iostream>

using namespace std;

int solution(string s) {
    int answer = 0;
    int i = 0;
    while (i < s.size()) {
        cout << i << s[i] << endl;
        if (s[i] == 'z') {
            answer *= 10;
            i += 4;
        }
        else if (s[i] == 'o') {
            answer *= 10;
            answer += 1;
            i += 3;
        }
        else if (s[i] == 't') {
            if (s[i+1] == 'w') {
                answer *= 10;
                answer += 2;
                i += 3;
            }
            else {
                answer *= 10;
                answer += 3;
                i += 5;
            }
            
        }
        else if (s[i] == 'f') {
            if (s[i+1] == 'o') {
                answer *= 10;
                answer += 4;
                i += 4;
            }
            else {
                answer *= 10;
                answer += 5;
                i += 4;
            }
            
        }
        else if (s[i] == 's') {
            if (s[i+1] == 'i') {
                answer *= 10;
                answer += 6;
                i += 3;
            }
            else {
                answer *= 10;
                answer += 7;
                i += 5;
            }
            
        }
        else if (s[i] == 'e') {
            answer *= 10;
            answer += 8;
            i += 5;
        }
        else if (s[i] == 'n') {
            answer *= 10;
            answer += 9;
            i += 4;
        }
        else {
            answer *= 10;
            answer += (int)s[i];
            answer -= (int)'0';
            i++;
        }
    }
    return answer;
}