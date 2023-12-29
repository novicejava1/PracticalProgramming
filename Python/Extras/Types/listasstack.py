stack = ["eat", "sleep", "drink", "work"]
stack.append("listen")
stack.append("Excerise")

print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

i = range(10)
print("*"*100)
for i in range(len(stack)):
    print(stack)
    stack.pop()

