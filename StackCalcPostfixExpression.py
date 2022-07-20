from Stack import Stack
import operator

class OperationMaker:
    def __init__(self):
        self.operations = {'+': operator.add, '*': operator.mul}
        
    def is_operation(self, token):
        return (token in self.operations)

    def get_operation(self, token):
        return self.operations[token]

def make_num(token):
    num = None
    try:
        num = int(token)
    except ValueError:
        pass
    return num

# This function is written under assumption that each token of the 
# given expression is wrapped by at least one space symbol
def calc_postfix_expression(expressionString):
    numStack = Stack()
    operationMaker = OperationMaker()
    result = 0    
    
    emptyToken = ''
    equalSign  = '='
    space  = ' '

    tokens = expressionString.split(space)    
    
    for token in tokens:        
        if token == emptyToken:            
            continue
        
        num = numStack.peek()
        if token == equalSign and num is None:
            raise ValueError("Nothing was calculated yet")
        if token == equalSign:
            return num
        
        num = make_num(token)
        if num is not None:
            numStack.push(num)
            continue
            
        if not operationMaker.is_operation(token):
            raise ValueError("Invalid symbol", token)
            
        operation = operationMaker.get_operation(token)
        op1 = numStack.pop()
        op2 = numStack.pop()
        if op1 is None or op2 is None:
            raise ValueError("Too much operators in expression", expressionString)
        result = operation(op1, op2)
        numStack.push(result)
    
    return result