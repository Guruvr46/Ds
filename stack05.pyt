import queue

stack = queue.LifoQueue()
stack.put(10)
stack.put(90)
stack.put(50)
print(stack.get())


stack2 = queue.LifoQueue(3)
stack2.put(2)
stack2.put(89)
stack2.put(0)

print(stack2.get())
print(stack2.get())

print(stack2.get())

print(stack2.get(timeout=2))
