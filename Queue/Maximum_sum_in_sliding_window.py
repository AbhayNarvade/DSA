def maxSlidingWindow(arr, k):
    i = 0
    result = []

    while i + k <= len(arr):
        a = arr[i]
        for j in range(i, i + k):
            if arr[j] > a:
                a = arr[j]
        result.append(a)
        i += 1

    print(result)


from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []

        for i in range(len(nums)): 

            # Remove elements out of window
            if dq and dq[0] == i - k:
                dq.popleft()

            # Remove smaller elements from back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Add max to result when window is valid
            if i >= k - 1:
                result.append(nums[dq[0]])

        print(result)


if __name__ == "__main__":
    # with brute force approach 
    maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
    d1 = Solution()
    # without brute force approach
    d1.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
