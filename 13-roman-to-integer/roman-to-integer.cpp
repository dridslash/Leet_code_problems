class Solution {
public:
    int romanToInt(string s) {
        int Number = 0;
        int len = 0;
        for( ; len < s.length(); len++){
            // std::cout << s[len] << std::endl;
            if (s[len] == 'I'){
                if (s[len + 1] && s[len + 1] == 'V'){
                    Number += 4;
                    len++;
                }
                else if (s[len + 1] &&  s[len + 1] == 'X'){
                    Number += 9;
                    len++;
                }
                else
                    Number ++;
            }
            else if (s[len] == 'V'){
                Number += 5;
            }
            else if (s[len] == 'X'){
                if (s[len + 1] &&  s[len + 1] == 'L'){
                    Number += 40;
                    len++;
                }
                else if (s[len + 1] &&  s[len + 1] == 'C'){
                    Number += 90;
                    len++;
                }
                else
                    Number += 10;
            }
            else if (s[len] == 'L'){
                Number += 50;
            }
            else if (s[len] == 'C'){
                if (s[len + 1] && s[len + 1] == 'D'){
                    Number += 400;
                    len++;
                }
                else if (s[len + 1] && s[len + 1] == 'M'){
                    Number += 900;
                    len++;
                }
                else
                    Number += 100;
            }
            else if (s[len] == 'D'){
                Number += 500;
            }
            else if (s[len] == 'M'){
                Number += 1000;
            }
        }
        return (Number);
    }
};