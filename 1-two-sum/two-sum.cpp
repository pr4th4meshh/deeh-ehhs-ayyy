using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashMap;
        for(int i=0; i < nums.size(); i++) {
            int ans = target - nums[i];
            cout<<ans<<endl;
            if(hashMap.count(ans)) { // returns 1 if true or 0
                return {
                    hashMap[ans], i // hashMap[invalid_index], index_where_el_was_found
                };
            }
            hashMap[nums[i]] = i; 
        }
        return {};
    }
};