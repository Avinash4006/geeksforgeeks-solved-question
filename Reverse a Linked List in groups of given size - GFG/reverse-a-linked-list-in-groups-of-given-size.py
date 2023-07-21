"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_linked_list(self, head, k):
        prev = None
        current = head
        for _ in range(k):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev, head, current

    def reverse(self, head, k):
        if not head or k <= 1:
            return head

        # Helper function to count the number of nodes in the list
        def count_nodes(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count

        num_nodes = count_nodes(head)

        # If k is greater than or equal to the number of nodes, reverse the entire list
        if k >= num_nodes:
            return self.reverse_linked_list(head, k)[0]

        prev_tail = None
        new_head = None
        current = head

        while num_nodes >= k:
            prev, group_start, current = self.reverse_linked_list(current, k)

            if not new_head:
                new_head = prev

            if prev_tail:
                prev_tail.next = prev

            prev_tail = group_start
            num_nodes -= k

        # If there are any remaining nodes, reverse them as a separate group
        if num_nodes > 0:
            prev_tail.next, _, _ = self.reverse_linked_list(current, num_nodes)

        return new_head


#{ 
 # Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        ob=Solution()
        new_head = ob.reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1




# } Driver Code Ends