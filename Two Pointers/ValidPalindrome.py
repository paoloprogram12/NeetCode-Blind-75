class Solution:
    def isPalindrome(self, s: str) -> bool: 

        filtered_s = []
        for ch in s:
            if ch.isalnum(): # only keeps letters and digits
                filtered_s.append(ch.lower()) # converts to lowercase

        s = "".join(filtered_s)

        l_p = 0
        r_p = len(s) - 1

        while l_p < r_p:
            if s[l_p] != s[r_p]:
                return False
            l_p += 1
            r_p -= 1
            
        return True
            

        
def main():
    s = "Was it a car or a cat I saw?"
    arr = []

    for i in s:
        if i != " ":
            arr.append(i)

    for i in range(len(arr)):
        print(arr[i])

if __name__ == "__main__":
    main()