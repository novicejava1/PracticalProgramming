from collections import deque

queue = deque(["Teddy", "Beddy", "Muddy", "Studdy"])
#print(dir(queue))
queue.extendleft(["Mike", "Bike", "Like"])
print(queue)

