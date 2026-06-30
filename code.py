class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        maxnum=0
        for i in range(k):
            maxnum+=nums[i]
        mo=maxnum
        for i in range(k,n):
            mo=(mo+nums[i]-nums[i-k])
            maxnum=max(maxnum,mo)
            print(maxnum)
        return maxnum/k
        
