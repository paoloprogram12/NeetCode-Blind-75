from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {} # val : index

        for i, n in enumerate(nums): # enumerate gives a pair of numbers (index, value)
            diff = target - n
            if diff in prev:
                return [prev[diff], i]
            prev[n] = i
        return
    

def main():
    print("mongus")
    test = Solution()
    fort = [4, 5, 6]
    sub = test.twoSum(fort, 7)
    print(sub)


if __name__ == "__main__":
    main()