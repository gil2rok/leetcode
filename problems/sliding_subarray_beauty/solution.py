class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = [0] * (len(nums)-k+1)
        freq = [0] * 50
        for i in range(k):
            if nums[i] < 0: freq[50 + nums[i]] += 1
        cnt = 0
        for idx in range(len(freq)):
            if freq[idx] > 0: cnt += freq[idx]
            if cnt >= x: 
                ans[0] = idx - len(freq)
                break

        # print(nums[0:k])
        # print(freq)
        # print(ans)
        # print()
        for i in range(1, len(nums)-k+1):
            j = i + k - 1

            # update subarray of size k
            if nums[i-1] < 0: # remove left element
                freq[50 + nums[i-1]] -= 1
            if nums[j] < 0: # add right element
                freq[50 + nums[j]] += 1

            # find k-th smallest element
            cnt = 0
            for idx in range(len(freq)):
                if freq[idx] > 0: cnt += freq[idx]
                if cnt >= x: 
                    ans[i] = idx - len(freq)
                    break

            # print(nums[i:j+1])
            # print(freq)
            # print(ans)
            # print()
            
        return ans