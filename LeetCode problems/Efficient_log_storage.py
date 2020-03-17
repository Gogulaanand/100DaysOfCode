# You run an e-commerce website and want to record the last N order ids in a log. 
# Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N. 
# You should be as efficient with time and space as possible.




class Order:
    
    def __init__(self, size):
        self.storage = list()
        self.size = size 
    
    def record(self, item):
        self.storage.append(item)
        if len(self.storage)>self.size:
            self.storage = self.storage[1:]

    def get_last(self, index):
        return self.storage[-index]
    
log = Order(5)
log.record(1)
log.record(2)

assert log.storage == [1,2]

log.record(3)
log.record(4)
log.record(5)
log.record(6)

assert log.storage == [2,3,4,5,6]
assert len(log.storage) == 5

assert log.get_last(1) == 6
assert log.get_last(3) == 4


    