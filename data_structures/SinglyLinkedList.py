class Node:

    def __init__(self, val, nextNode=None):
        # Nodes with no nextNode have nextNode as None
        self.val = val
        self.nextNode = nextNode


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        thisNode = self.head
        if thisNode == None:
            return -1

        currentPtr: int = 0
        while currentPtr < index and thisNode:
            currentPtr += 1
            thisNode = thisNode.nextNode

        if not thisNode:
            return -1

        return thisNode.val

    def insertHead(self, val: int) -> None:
        currentHead = self.head
        if not currentHead:
            self.head = Node(val, None)
            self.tail = self.head
        else:
            self.head = Node(val, currentHead)

    def insertTail(self, val: int) -> None:
        newTail = Node(val, None)
        if not self.head:
            self.insertHead(val)
        else:
            newTail = Node(val, None)
            self.tail.nextNode = newTail
            self.tail = newTail

    def remove(self, index: int) -> bool:
        if self.head == None:
            return False
        elif index == 0:
            self.head = self.head.nextNode
            return True

        i = 1
        leftNode = self.head

        while i < index and leftNode:  # Iterate the node before the one to be removed
            leftNode = leftNode.nextNode
            i += 1

        print(leftNode.val)

        if not leftNode or not leftNode.nextNode:  # If out of bounds
            return False
        elif leftNode.nextNode == self.tail:  # If the item to remove is the tail
            # print("To remove is the tail!")
            self.tail = leftNode
            leftNode.nextNode = None
            # print(f"Tail next node: {self.tail.nextNode}")
            # print(f"leftNode nextNode: {leftNode.nextNode}")
        else:  # In the middle
            removeNode = leftNode.nextNode
            rightNode = removeNode.nextNode
            leftNode.nextNode = rightNode
            removeNode.nextNode = None
        return True

    def getValues(self) -> list[int]:
        retList = []
        thisNode = self.head
        while thisNode:
            retList.append(thisNode.val)
            thisNode = thisNode.nextNode

        return retList


if __name__ == "__main__":

    # [
    #     "insertHead",
    #     1,
    #     "insertHead",
    #     2,
    #     "insertTail",
    #     3,
    #     "insertTail",
    #     4,
    #     "insertHead",
    #     5,
    #     "get",
    #     0,
    #     "get",
    #     2,
    #     "get",
    #     4,
    #     "remove",
    #     2,
    #     "remove",
    #     0,
    #     "insertHead",
    #     6,
    #     "insertTail",
    #     7,
    #     "getValues",
    #     "get",
    #     5,
    # ]
    l = LinkedList()
    l.insertHead(1)
    l.insertHead(2)
    l.insertTail(3)
    l.insertTail(4)
    l.insertHead(5)
    l.get(0)
    l.get(2)
    l.get(4)
    l.remove(2)
    l.remove(0)
    l.insertHead(6)
    l.insertTail(7)
    print(l.getValues())
    assert l.get(5) == -1

    # ["insertTail", 1, "insertTail", 2, "get", 1, "remove", 1, "insertTail", 2, "get", 1, "get", 0]

    # l = LinkedList()
    # l.insertTail(1)
    # l.insertTail(2)
    # l.get(1)
    # l.remove(1)
    # l.insertTail(2)
    # l.get(1)
    # l.get(0)

    # l = LinkedList()
    # l.insertHead(1)
    # l.insertHead(2)
    # print(l.head.val)
    # print(l.tail.val)
    # l.insertTail(0)
    # print(l.tail.val)
    # print(l.head.val)
    # print(l.head.nextNode.nextNode.val)
    # assert l.get(0) == 2
    # assert l.get(1) == 1
    # assert l.get(2) == 0

    # Test removeNode

    # l.remove(0)
    # print(l.head.val)
    # print(l.head.nextNode.val)
    # print(l.head.nextNode.nextNode)  # Should be none

    # l.insertHead(2)
    # l.remove(1)

    # print(l.getValues())
