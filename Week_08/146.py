class ListNode:
    #双向链表
    def __init__(self,key = None, value = None):
        self.key = key
        self.value = value 
        self.prev = None
        self.next = None 

class LRUCache:
    #最近最少使用缓存，采用字典+双向链表
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()
        #self.head.prev = self.tail
        self.head.next = self.tail
        self.tail.prev = self.head
        #self.tail.next = self.head

    def move_node_to_tail(self,key: int) -> None:
        #从hashmap中取出key对应的节点，此处不用再判断node是否为空，在get和put中判断
        node = self.hashmap[key]
        #调整node的前后节点
        node.prev.next = node.next
        node.next.prev = node.prev
        #调整尾节点
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.move_node_to_tail(key)
            return self.hashmap.get(key).value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.move_node_to_tail(key)
            self.hashmap[key].value = value
        else:
            if self.capacity == len(self.hashmap):
                #pop hash表对应项
                self.hashmap.pop(self.head.next.key)
                #调整头指针
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            newNode = ListNode(key,value)
            self.hashmap[key] = newNode
            #插入最后
            newNode.prev = self.tail.prev
            newNode.next = self.tail
            self.tail.prev.next = newNode
            self.tail.prev = newNode

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))       # 返回  1
cache.put(3, 3)    # 该操作会使得关键字 2 作废
print(cache.get(2))       # 返回 -1 (未找到)
cache.put(4, 4)    # 该操作会使得关键字 1 作废
print(cache.get(1))       # 返回 -1 (未找到)
print(cache.get(3))       # 返回  3
print(cache.get(4))       # 返回  4

