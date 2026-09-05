from collections import deque
# dequeは両端キューなのでfrontからもbackからも取り出せる
queue = deque()

queue.append(1)
queue.append(2)
print(queue)

queue.popleft()
print(queue)
queue.popleft()
print(queue)

queue.appendleft(1)
queue.appendleft(2)
print(queue)

queue.pop()
print(queue)
queue.pop()
print(queue)