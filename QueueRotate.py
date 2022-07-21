from Queue import Queue

def rotate_queue(queue, n):    
    if queue.size() == 0:
        return
    for i in range(0,n):
        val = queue.dequeue()
        queue.enqueue(val)