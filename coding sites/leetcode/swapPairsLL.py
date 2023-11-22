class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def swapPairs(head):
    """
    Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without
    modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
    link: https://leetcode.com/problems/zigzag-conversion/
    :param head: Optional([ListNode])
    :return: Optional([ListNode])
    """
    # Start with a dummy node which points to the head
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next and current.next.next:
        # Identify the nodes to be swapped
        first = current.next
        second = current.next.next

        # Swap the nodes
        first.next = second.next
        second.next = first
        current.next = second

        # Move to the next pair
        current = first

    return dummy.next


# Helper function to create a linked list from a list
def createLinkedList(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Helper function to print the linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


if __name__ == "__main__":
    # Create a linked list and test the swapping function
    lst = [1, 2, 3, 4, 5, 6]
    head = createLinkedList(lst)
    print(head.next.value)
    print("Original Linked List:")
    printLinkedList(head)

    # Swap the pairs
    swapped_head = swapPairs(head)
    print("\nLinked List after Swapping Pairs:")
printLinkedList(swapped_head)
