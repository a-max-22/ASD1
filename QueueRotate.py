from Queue import Queue

def rotate_queue(queue, n):
    for i in range(0,n):
        val = queue.dequeue()
        if val is None:
            return 
        queue.enqueue(val)