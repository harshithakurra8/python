#Queues 

#Objective: Implement a queue using a list. 

#Concept: Print Job Queue. 

#Tasks: 

#Implement enqueue, dequeue, and front operations for managing print jobs. 

#Use decorators to log job additions and removals. 

import functools

def log_enqueue(func):
    """Decorator to log enqueue operations."""
    @functools.wraps(func)
    def wrapper_log_enqueue(*args, **kwargs):
        job = args[1]                                                     # The job is the second argument to enqueue method
        print(f"Enqueue: Adding job '{job}' to the queue.")
        result = func(*args, **kwargs)
        return result
    return wrapper_log_enqueue

def log_dequeue(func):
    """Decorator to log dequeue operations."""
    @functools.wraps(func)
    def wrapper_log_dequeue(*args, **kwargs):
        if args[0].is_empty():
            print("Dequeue: Queue is empty. No job to remove.")
        else:
            job = args[0].front()                                                   # Get the job at the front
            print(f"Dequeue: Removing job '{job}' from the queue.")
        result = func(*args, **kwargs)
        return result
    return wrapper_log_dequeue

class PrintJobQueue():
    def __init__(self):
        self.queue = []

    @log_enqueue
    def enqueue(self, job):
        self.queue.append(job)

    @log_dequeue
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        return len(self.queue) == 0

print_queue = PrintJobQueue()

# Enqueue jobs
print_queue.enqueue("Print job 1")
print_queue.enqueue("Print job 2")
print_queue.enqueue("Print job 3")

# Check the front job
print(f"Front job: {print_queue.front()}")  # Output: Front job: Print job 1

# Dequeue jobs
print_queue.dequeue()
print_queue.dequeue()
print_queue.dequeue()
print_queue.dequeue()  # Trying to dequeue from an empty queue
