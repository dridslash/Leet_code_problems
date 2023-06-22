class Solution {
public:
    bool isAnagram(string s, string t) {
        std::sort(t.begin(),t.end(),std::greater<char>());
        std::sort(s.begin(),s.end(),std::greater<char>());
        if (s.compare(t) == 0)
            return true;
        return false;
    }
};