class Solution:
    def isValid(self, s: str) -> bool:
        map = {')' : '(', ']' : '[', '}' : '{'}
        stack = []
        
        for c in s:
            if c not in map:
                stack.append(c)
                continue
            if not stack or (map[c] != stack[-1]):
                return False
            stack.pop()
            
        return not stack
            
#     def isValid(self, s: str) -> bool:
#         stack = []
        
        
#         for c in s:
#             # add open paren to stack
#             if c == '(' or c=='[' or c == '{':
#                 stack.append(self.opposite(c))
                
#             # if have close paren, check that it is on top of stack
#             # (and also check that stack is not empty) 
#             else:
#                 if len(stack) == 0 or c != stack[-1]:
#                     return False
#                 stack.pop()
#         return len(stack) == 0
    
    def opposite(self, c):
        if c == '(':
            return ')'
        elif c == '[':
            return ']'
        else:
            return '}'