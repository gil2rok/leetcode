class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            #print(c, '\tStack: ', stack)
            # add open paren to stack
            if c == '(' or c=='[' or c == '{':
                stack.append(self.opposite(c))
            else:
                if len(stack) == 0 or c != stack[-1]:
                    return False
                stack.pop()
        return len(stack) == 0
    
    def opposite(self, c):
        if c == '(':
            return ')'
        elif c == '[':
            return ']'
        else:
            return '}'