

input_stack = []

def stack_push():
    n = int(input("Enter number of elements to push into the stack "))
    print("Enter elements of stack: ")
    for i in range(0, n):
        stack_elements = input()
        input_stack.append(stack_elements)
    print("Stack after adding elements")
    print(input_stack)


def stack_pop():
    n = int(input("Enter number of elements to pop from the stack "))
    for i in range(0, n):
        input_stack.pop()
    print("Stack after popping elements is ")
    print(input_stack)


def is_stack_empty(stack):
    return len(stack) == 0


stack_push()
stack_pop()

if is_stack_empty(input_stack):
    print("Stack is empty")
else:
    print("Stack is not empty")

