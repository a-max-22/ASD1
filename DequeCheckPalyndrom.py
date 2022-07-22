from Deque import Deque

def check_palyndrom(string):
    deque = Deque()
    for i in string:
        deque.addTail(i)
        
    while deque.size() > 1:
        if deque.removeFront() != deque.removeTail():
            return False
            
    return True