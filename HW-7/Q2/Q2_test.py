from remove_dups_linked_list import Node 
from remove_dups_linked_list import LinkedList 


def test_happy_path():
    first_node = Node()
    first_node.set_data(11)
    linked_list = LinkedList(first_node)
    assert linked_list.head.data==11, "test for set_data(), it should be 11"
    linked_list.insert(3)
    assert linked_list.head.next.data==3, "test for insert(), it should be 3"
    linked_list.insert(6)
    linked_list.insert(3)
    linked_list.insert(11)
    linked_list.insert(6)
    linked_list.insert(5)
    linked_list.insert(7)
    linked_list.insert(5)
    linked_list.remove_dups()
    tmp=[]
    current = linked_list.head
    while current!=None:
        tmp.append(current.data)
        current=current.next
    assert tmp == [11, 3, 6, 5, 7], "test for remove_dups(), should return [11, 3, 6, 5, 7]"
    assert linked_list.size()==5, "test for size() , should be 5"
    assert [linked_list.print_list()]== [None], "test for print_list(), return type should be None"
    
def test_edge_cases():
    import pytest
    first_node = Node()
    linked_list = LinkedList(first_node)
    assert linked_list.head.data==None, "if nothing is in Node, head.data should be None"
    linked_list.head=None
    linked_list.size()
    assert linked_list.size()==0, "if head is None, it should return size 0"
    linked_list.insert(3)
    assert linked_list.head.data==3, "if the head is None, the insert data is head.data"
    first_node = Node()
    linked_list = LinkedList(first_node)
    linked_list.insert(None)
    assert linked_list.head.data==None, "if insert None data, the head.data should be None"
    with pytest.raises (ValueError):
        linked_list.head=None
        linked_list.print_list()