# Linked list example


# the Node class
class Node(object):
    # 这种用法表示Python中特殊的方法名。其实，这只是一种惯例，对Python系统来说，这将确保不会与用户自定义的名称冲突。通常，你将会覆写这些方法，并在里面实现你所需要的功能，以便Python调用它们。
    # These are special method names used by Python. As far as one’s concerned, this is just a convention, a way for the Python system to use names that won’t conflict with user-defined names. You then typically override these methods and define the desired behaviour for when Python calls them. For example, you often override the __init__ method when writing a class.
    def __init__(self, val): 
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


# the LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        # TODO: insert a new node
        new_node = Node(data)

    def find(self, val):
        # TODO: find the first item with a given value
        item = self.head

        return None

    def deleteAt(self, idx):
        # TODO: delete an item at given index
        if idx > self.count-1:
            return

    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()


# create a linked list and insert some items
itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)
itemlist.dump_list()

# exercise the list
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(13))
print("Finding item: ", itemlist.find(78))

# delete an item
# itemlist.deleteAt(3)
# print("Item count: ", itemlist.get_count())
# print("Finding item: ", itemlist.find(38))
# itemlist.dump_list()
