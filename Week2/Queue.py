
input_queue = []


def enqueue():
    n = int(input("Enter number of elements to add into the queue "))
    print("Enter elements of queue: ")
    for i in range(0, n):
        queue_elements = input()
        input_queue.append(queue_elements)
    print("Queue after adding elements")
    print(input_queue)


def dequeue():
    n = int(input("Enter number of elements to remove from the queue "))
    for i in range(0, n):
        input_queue.pop(0)
    print("Queue after popping elements is ")
    print(input_queue)


def is_queue_empty(input_queue):
    return len(input_queue) == 0


enqueue()
dequeue()
if is_queue_empty(input_queue):
    print("Queue is empty")
else:
    print("Queue is not empty")