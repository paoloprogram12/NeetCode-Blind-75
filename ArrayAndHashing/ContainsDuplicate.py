from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
        
def main():
    arr = [1, 2, 3, 3]
    fort = Solution()
    result = fort.hasDuplicate(arr)
    print(result)

    print ("-------------")

    arr = [1, 2, 3, 4]
    result = fort.hasDuplicate(arr)
    print(result)

if __name__ == "__main__":
    main()