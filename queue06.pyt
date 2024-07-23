import queue
q = queue.Queue()

q.put(10)
q.put(50)
q.put(2)

print(q)

print(q.get())