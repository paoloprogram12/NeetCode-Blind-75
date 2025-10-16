from typing import List

class Solution:
    def findMIn(self, nums: List[int]) ->int:
        return ...
    
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
    s = Search()
    arr = [1, 7, 14, 32, 8, 6, 7, 67, 43, 2]
    arr.sort()
    low = 0
    high = len(arr) - 1
    result = s.binSearch(arr, 67, low, high) # should return 9
    print(result)

if __name__ == "__main__":
    main()