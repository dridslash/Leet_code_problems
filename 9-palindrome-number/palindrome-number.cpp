class Solution {
public:
    bool isPalindrome(int x) {
    std::string Number;
    std::string Number_reversed;
    Number = Number_reversed = std::to_string(x);
    std::reverse(Number_reversed.begin(),Number_reversed.end());
    // std::cout << "Number reversed --> " << Number_reversed << std::endl;
    // std::cout << "Number  --> " << Number << std::endl;
    if (Number_reversed.compare(Number) == 0)
        return(true);
    return (false);
    }
};