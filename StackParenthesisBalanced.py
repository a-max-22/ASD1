from Stack import Stack

def parenthesis_balanced(string):
    if (string  == ''):
        raise ValueError("Empty string")
        
    stack  = Stack()
    openP  = '('
    closeP = ')'
    
    for c in string:
        if  (c != openP and c != closeP):
            raise ValueError("Unexpected symbol", c)
        if (c == closeP and stack.pop() is None):
            return False
        if (c == openP):
            stack.push(c)

    return (stack.size() == 0)