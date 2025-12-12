using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashMap;
        for(int i=0; i < nums.size(); i++) {
            int ans = target - nums[i];
            if(hashMap.count(ans)) { 
                return { hashMap[ans], i };
            }
            hashMap[nums[i]] = i; 
        }
        return {};
    }
};