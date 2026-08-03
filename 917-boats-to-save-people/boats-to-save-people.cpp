class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());

        int res = 0;
        int left = 0;
        int right = people.size() - 1;

        while(left <= right) {
            int remaining = limit - people[right];
            right -= 1;
            res += 1;

            if(left <= right && remaining >= people[left]) {
                left += 1;
            }
        }
        return res;

    }
};