class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT
    
def main():
    fort = "fortnite"
    nite = Solution()
    result = nite.isAnagram("nite", "nite")
    print(result)


if __name__ == "__main__":
    main()