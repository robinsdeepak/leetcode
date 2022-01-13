class Solution {
public:
vector<int> maxSlidingWindow(vector<int>& nums, int k)
{
vector<int> mv;
if (k == 1) return nums;
map<int,int> freq;
for (int i=0; i<k; i++)
freq[nums[i]]++;
mv.push_back(freq.rbegin()->first);
for(int i=k; i<nums.size(); i++)
{
freq[nums[i-k]]--;
if (freq[nums[i-k]] == 0)
{
freq.erase(freq.find(nums[i-k]));
}
​
freq[nums[i]]++;
mv.push_back(freq.rbegin()->first);
}
return mv;
}
};
​
​