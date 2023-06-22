class Solution {
public:
    bool isAnagram(string s, string t) {
        int pos;
        if (s.size() != t.size())
            return false;
        else{
            for(int i = 0 ; i < s.size(); i++){
                pos = t.find(s[i]);
                if (pos != std::string::npos){
                    t.erase(t.begin() + pos);
                }
                else
                    return false;
            }
        }
        return true;
    }
};