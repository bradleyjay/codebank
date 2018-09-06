'''

Linked List: 

List class:
1) Constructor: NODE: value, next.
2) Constructor: LIST: Head pointer 
3) Add
4) Traversal Functions: (End of List ) Pop, Append
5) Traversal Functions: (Position) Size, Search, Delete 


'''

# 1) Constructor: NODE: value, next

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# 2) Constructor: LIST: head pointer

class Linked_List:
    def __init__(self):
        self.head = None


# 3) Add

    def add(self, value):
        n = Node(value)
        n.next = self.head
        self.head = n

# 4) Traversal Functions (END OF LIST)

    #POP

    def pop(self):

        # safety/head action
        if self.head == None:
            return False

        # traversal
        current = self.head
        previous = None

        while current.next != None:

            previous = current
            current = current.next

        # action
         popped = current.value

        if previous == None:    
            self.head = None
        else:
            previous.next = None 
        
        return popped

    #APPEND
    def append(self,value):
        
        # safety/head action
        if self.head == None:
            self.head = Node(value)
            return 

        # traversal 
        current = self.head
        previous = None

        while current.next != None

            previous = current          # for consistency
            current = current.next

        # action
        current.next = Node(value)

    # 5) Traversal:  (position) Search, Size, Delete

        # search
        def search(self, value):

            #safety/head
            if self.head == None:
                return False

            # traversal
            current = self.head
            previous = None

            while current.next != None:

                if current.value == value:
                    return True

                previous = current
                current = current.next

            #action

            return False

        # Size
        def size(self):

            #safety / head
            if self.head == None:
                return 0

            # traversal
            current = self.head
            previous = None
            count = 0
            
            while current.next != None:

                previous = current
                current = current.next
                count +=1

            #action    
            return count

        def delete(self,value):

            # safety/head
            if self.head == None:
                return False

            #traversal

            current = self.head
            previous = None

            while current.next != None:

                if self.value == value:
                    previous.next = current.next
                    return 

                previous = current
                current = current.next

            # action
            return False



#####################
######## tests




a = Linked_List()
a.add('purple')
print(a.head.value)
a.pop()
print(a.head)
