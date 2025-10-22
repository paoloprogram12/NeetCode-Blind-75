from typing import List

class Solution:
    def findMIn(self, nums: List[int]) ->int:
        left = 0, right = len(nums) - 1
        result = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left]) # gets the minimum number between the two values
                break

            mid = (left + right) // 2
            result = min(result, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return result
    
# recursive binary search
# also has to be sorted first
class Search:
    def binSearch(self, arr: List[int], target: int, low: int, high: int) -> int:
            if low > high:
                return -1
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                return self.binSearch(arr, target, low, mid - 1)
            else:
                return self.binSearch(arr, target, mid + 1, high)
        
def main():

    # binary search test
    s = Search()
    arr = [1, 7, 14, 32, 8, 6, 7, 67, 43, 2]
    arr.sort()
    low = 0
    high = len(arr) - 1
    result = s.binSearch(arr, 67, low, high) # should return 9
    print(result)

if __name__ == "__main__":
    main()