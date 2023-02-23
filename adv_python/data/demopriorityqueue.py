import queue
q=queue.PriorityQueue()
q.put((-3,10))
q.put((-1,4))
q.put((-2,4))
q.put((-1,6))
while not q.empty():
    print(q.get()[1],end=' ')