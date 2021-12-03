from queue import Queue

def test_happy_path():
    obj = Queue()
    obj.enqueue(5)
    obj.enqueue(7)
    obj.enqueue(8)
    assert obj is not None, "The queue should not be None"
    assert obj.dequeue() == 5, "The deleted element should be 5"
    assert obj.size() == 2, "The size of the queue should be 2"

def test_edge_cases():
    obj = Queue()
    obj.enqueue(None)
    assert obj.dequeue()==None, "None insert input should return None"
    obj = Queue()
    assert obj.dequeue()==None, "when delete from a empty list, it should return None"