import collections
q = collections.deque()
print(q)

q.appendleft(90)
q.appendleft(21)
print(q)

q.pop()
q.pop()

q.append(10)
q.append(21)

q.popleft()


print(q)