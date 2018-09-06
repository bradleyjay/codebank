# Linked List

'''

1) Node class:
    Constructor: Value, Next

2) List Class:
    Constructor: Head


3) Add

4) Traversal: END OF LIST (Append, Pop)

5) Traversal: POSITION (Search, Size, Delete)




'''
# 1: Constructor: Node - value, next
class Node:
    def __init__(self, value):
        self.value = value     
        self.next = None    # blank

# 2: Constructor: Linked List - head
class Linked_List:
    def __init__(self):
        self.head = None    # blank

# 3 ADD
    def add(self, value):
        n = Node(value)     # Create
        n.next = self.head  # Attach head as next
        self.head = n       # Set new as head

# 4 Traversal - End of List: Append, Pop
    def append(self, value):

        # 1) Safety/Head Action
        if self.head == None:      # empty list? Append at head
            self.head = Node(value)
            return

        # 2) Traversal
        current = self.head     # start at head
        previous = None         

        while current.next != None:     # traverse til end

            previous = current
            current = current.next

        # 3) Action
        current.next = Node(value)      # make a node as next

    def pop(self):

        # 1) Safety/Head action
        if self.head == None:
            return

        # 2) Traversal

        current = self.head
        previous = None

        while current.next != None:

            previous = current
            current = current.next

        # 3) Action

        popped = current.value

        if previous == None:    
            self.head = None
        else:
            previous.next = None 
        
        return popped

    # 5: Traversal: Position - Size, Search, Delete

    def size(self):

        # 1) Safety / Head action
        if self.head == None:
            return 0

        # 2) Traversal

        current =  head
        previous = None
        i = 1

        while current.next != None:

            previous = current
            current = current.next
            i += 1

        # 3) Action

        return i

    def search(self, value):

        # 1) Safety / Head Action
        if self.head == None:
            return False

        if self.head.value == value:
            return True

        # 2) Traversal

        current = self.head
        previous = None
        found = False

        while current.next != None and found == False:

            if current.value == value:
                found = True

            previous = current
            current = current.next

        # 3) Action:

        return found, current, previous

    def delete(self, value):

        found, current, previous = self.search(value)
        if found == True:
            previous.next = current.next
