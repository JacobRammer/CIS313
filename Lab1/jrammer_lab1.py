from mealticket import *


class Queue:
    """
    A standard queue class. First in first out
    """

    def __init__(self, size):
        """
        Init method for queue class.
        :param size: the max size of the queue
        :return: void
        """

        self.head = None
        self.tail = None
        self.max_size = size
        self.current_size = 0
        # self.data = []  # will need to change datatype to linked list later

    def isEmpty(self):
        """
        Checks to see if the current queue is empty
        :return: true if empty, otherwise false
        """

        return self.current_size == 0

    def isFull(self):
        """
        Checks to see if the current queue is full
        :return: true if full, otherwise false
        """

        return self.max_size == self.current_size

    def front(self):
        """
        Display the front mealticket if the queue has data.
        If the queue is empty, return false. Do not modify
        the dataset.
        :return: mealticket or false
        """

        if self.isEmpty():
            return False
        return self.head.data

    def enqueue(self, ticket):
        """
        Enqueue a mealticket. Move the tail pointer back 1 and increase size
        :param ticket: Mealticket
        :return: true if successful, otherwise false
        """

        if isinstance(ticket, MealTicket):
            if self.isFull():
                return False
            if self.tail is None:  # node is empty
                self.head = Node(ticket)
                self.tail = self.head
            else:
                self.tail.next = Node(ticket)
                self.tail = self.tail.next
            self.current_size += 1
            return True
        return False  # if ticket is not a mealticket

    def dequeue(self):
        """
        Remove the ticket at the front of the queue
        :return: mealticket if queue has data, false if queue is empty
        """

        if self.isEmpty():
            return False
        ticket = self.head.data
        self.head = self.head.next
        self.current_size -= 1
        return ticket


class Stack:
    """
    Stacks are first in last out
    """

    def __init__(self, size):
        self.head = None
        self.max_size = size
        self.current_size = 0
        # self.data = []  # need to change to linked list

    def isEmpty(self):
        """
        Checks to see if the stack is empty
        :return: True is empty, otherwise false
        """

        return self.current_size == 0

    def isFull(self):
        """
        Checks to see if the stack is full
        :return: true if full, otherwise false
        """

        return self.current_size == self.max_size

    def push(self, ticket):
        """
        If the stack is empty, append the newest data to top of the stack
        :return: True if successful, otherwise false
        """

        if isinstance(ticket, MealTicket):  # only want to push mealtickets
            if self.isFull():
                return False
            if self.head is None:
                self.head = Node(ticket)
            else:
                new_node = Node(ticket)
                new_node.next = self.head  # lifo
                self.head = new_node
            self.current_size += 1
            return True

    def pop(self):
        """
        Get the last datatype from the top of the stack.
        :return: Mealticket if stack has data, otherwise false
        """

        if self.isEmpty():
            return False
        temp_val = self.head
        self.head = self.head.next
        temp_val.next = None
        self.current_size -= 1
        return temp_val.data

    def peek(self):
        """
        Peek at the first element of the stack without deleting the item
        :return: Mealticket is stack has data, otherwise false
        """

        if self.isEmpty():
            return False
        return self.head.data


class Node:
    """
    This class will be the node for the linked list
    """

    def __init__(self, data):
        self.data = data
        self.next = None  # Just like ll in c, start as NULL


def main():

    # test = Queue(2)
    # print(test.is_empty())
    # print(test.is_full())
    # print(test.enqueue("test"))
    # print(test.dequeue())

    # stack = Stack(2)
    # stack.current_size = 2
    # print(stack.is_empty())
    # print(stack.is_full())
    # print(stack.push("test"))
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.peek())

    # linked_list = LinkedList()
    # first = Node(1)
    # second = Node(2)
    # linked_list.newNode(first)
    # linked_list.newNode(second)
    # linked_list.displayList()

    # q = Queue(4)
    # print(f"Enqueue {q.enqueue(5)}")
    # print(f"Enqueue {q.enqueue(4)}")
    # print(f"Enqueue {q.enqueue(3)}")
    #
    # print(f"front: {q.front()}")
    # print(f"Dequeue {q.dequeue()}")
    # print(f"front: {q.front()}")
    # print(f"Enqueue {q.enqueue(20)}")
    # print(f"Dequeue {q.dequeue()}")
    # print(f"Dequeue {q.dequeue()}")
    # print(f"front: {q.front()}")

    # s = Stack(2)
    # print(f"Push {s.push(5)}")
    # print(f"Push {s.push(4)}")
    # print(f"Push {s.push(3)}")
    # print(f"pop {s.pop()}")
    # print(f"pop {s.pop()}")
    # print(f"peek {s.peek()}")

    # s = Stack(4)
    #
    # my_ticket = MealTicket("Jared's Breakfast")
    # my_ticket.addItem(("Eggs", 4.50))  # adding items as a tuple
    # my_ticket.addItem(("Bacon", 2.50))
    # my_ticket.addItem(("OJ", 1.00))
    #
    # print(f"Enqueue {s.push(my_ticket)}")
    # t = s.pop()
    # print(f"{t.display()}")

    # s = Stack(3)
    # print(s.push(ticket1))

    q = Queue(5)
    print(q.enqueue(ticket1))
    t = q.dequeue()
    print(t.display())


if __name__ == "__main__":
    main()
