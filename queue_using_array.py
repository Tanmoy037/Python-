import array

class Queue:
    def __init__(self):
        self.my_queue = array.array('i',[])
    
    def is_empty(self):
        if len(self.my_queue):
            return False
        else:
            return True

    def enqueue(self,element):
        self.my_queue.append(element)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty can't dequeue")
        else:
            self.my_queue.pop(0)

if __name__ == "__main__":
    queue = Queue()
    print(queue.my_queue)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.my_queue)
    queue.dequeue()
    print(queue.my_queue)
    queue.dequeue()
    print(queue.my_queue)
    queue.dequeue()
    print(queue.my_queue)
    queue.dequeue()