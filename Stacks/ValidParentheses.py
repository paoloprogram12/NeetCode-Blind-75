class Solution:
    def isValid(self, s: str) -> bool: # ([{}])
        stack = []

        for letter in s:
            if letter == '[' or letter == '(' or letter == '{':
                stack.append(letter)

            if letter == ']' or letter == ')' or letter == '}':
                if not stack:
                    return False
                
                top = stack[-1] # looks at the top of the stack

                if letter == ']' and top == '[':
                    stack.pop()
                elif letter == ')' and top == '(':
                    stack.pop()
                elif letter == '}' and top == '{':
                    stack.pop()

                else:
                    return False
                
        if not stack:
            return True
        else:
            return False
        
def main():
    print("sup world")

if __name__ == "__main__":
    main()