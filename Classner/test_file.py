class Stack:
   def is_valid_parenthese(self, str1):
        stack = []
        mdict = {"(": ")", "{": "}", "[": "]"}

        for i in str1:
            if i in mdict:
                stack.append(i)
            elif len(stack) == 0 or mdict[stack.pop()] != i:
                print(stack,i)
                return False
        return len(stack) == 0

print(Stack().is_valid_parenthese("(){}[]"))
print(Stack().is_valid_parenthese("()[{}]}"))
print(Stack().is_valid_parenthese("()"))
            
