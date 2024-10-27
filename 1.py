from array import *
value= array('i', [1,3,5,6,7])
for i in range(len(value)):
    print(value[i])

# searching in arrays

from array import *
value=array('i',[1,3,5,6,7])
print(list(value))
num=5
for i in range(len(value)):
    if value[i]==num:
        print(f"number {num} is found at index {i}")


 class node:
   def __init__(self ,data):
         self.data=data
         self.next=None
 class linklist:
     def __init__(self):
         self.head=None
     def app(self,data):
         new_node=node(data)
         if self.head is None:
             self.head=new_node
             return
         last=self.head
         while last.next:
             last=last.next
         last.next=new_node
     def print(self):
         temp=self.head
         while temp:
             print(temp.data,end="-->")
             temp=temp.next
         print("None")


 list=linklist()
 list.app(10)
 list.app(16)
 list.app(17)
 list.app(18)
 list.print()



# list=[]
# list.append(1)
# list.append(2)
# list.append(3)
# print(list)
# list.pop()
# print(list)
# list.pop()
# list.pop()
# print(list)

# import  queue from collections 

# string="another"
# index=0
# for i in string:
#     print(i)
#     print(index)
#     index+=1

# str=input("rntert te valur")
# for i in range(len(str)):
#     for j in range(len(str)-1,0,-1):
#         if str[j]==str[i]:
#             print("pal")
#             break
#         else:
#             print("not pal")


# str=input("rntert te valur")
# right=len(str)-1
# left=0
# while right>left:
#     if str[right]!=str[left]:
#         print("not pal")
#         right-=1
#         left+=1
   
# LIST_1 = [1, 3, 5, 7]
# LIST_2 = [2, 4, 6, 8]
# print(LIST_1 + LIST_2)
# LIST_1 * 3
# print(LIST_1 == LIST_2)
# 5 in LIST_1
# 10 in LIST_1


# class Solution(object):
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         l = 0
#         r = len(nums)-1
#         if nums[l] > target:
#             return 0
#         if nums[r] < target:
#             return r+1
#         while l <= r:
#             if nums[r] == target:
#                 return r
#             elif nums[r] < target:
#                 return r+1
#             r -= 1

#             if nums[l] == target:
#                 return l
#             elif nums[l] > target:
#                 return l
#             l += 1
#         return l
    

# class Solution(object):
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         for i in range(len(nums)):
#             right=len(nums)-1
#             left= 0
#             while right>=left:
#                 mid=(right+left)//2
#                 if nums[mid]<target:
#                     left=mid+1
#                 elif nums[mid]>target:
#                     right=mid-1
#                 else:
#                     return mid
#             return left
        

# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         if len(haystack)<len(needle):
#             return -1
#         for i in range(len(haystack)):
#             if haystack[i:i+len(needle)]==needle:
#                 return i
#         return -1


# list=[1,2,3,4,5,6,7,8,9,10]
# for  i in range(0,len(list)-1,2):
#     temp=list[i+1]
#     list[i+1]=list[i]
#     list[i]=temp
# print(list)


# a= 5
# for i in range(a):
#     print(" "*(a-i)+"* "*(i+1))

# for row in range(7): # 0 to 6
#     for col in range(5): # 0 to 4
#         if row == 0 and (col in {1,2,3}):
#             print("*", end=" ")
#         elif row in {1,2,4,5,6} and (col in {0,4}):
#             print("*", end=" ")
#         elif row == 3:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()                                  
  


# class MyQueue:
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []

#     def push(self, x: int) -> None:
#         self.stack1.append(x)

#     def pop(self) -> int:
#         self.peek()  # Ensure stack2 has the current front element
#         return self.stack2.pop()

#     def peek(self) -> int:
#         if not self.stack2:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#         return self.stack2[-1]

#     def empty(self) -> bool:
#         return not self.stack1 and not self.stack2

# # Example usage
# queue = MyQueue()
# queue.push(1)
# queue.push(2)
# print(queue.peek())  # Output: 1
# print(queue.pop())   # Output: 1
# print(queue.empty()) # Output: False


# class Node:
#     def __init__(self,data,next=0):
#         self.data=data
#         self.next=None
# class linklist:
#     def  __init__(self):
#         self.head=None
#     def add(self,data):
#         newnode=node(data,self.head)
#         self.head=newnode
#     def print(self):
#         current=self.head
#         while current:
#             print(current.data,end=" ")
#             current=current.next
# link=linklist()
# linklist.add(3)
# linklist.add(4)
# linklist.print()
# class linklist:
#     def  __init__(self):
#         self.head=None
    
#     def insertAtBegin(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         else:
#             new_node.next = self.head
#             self.head = new_node
#     def printLL(self):
#         current_node = self.head
#         while(current_node):
#             print(current_node.data ,  end="--> ")

#             current_node = current_node.next

# # Example usage
# link = linklist()
# link.insertAtBegin(1)
# link.insertAtBegin(2)
# link.insertAtBegin(3)
# link.printLL()  


class node:
    def __init__(self,data ,next=0):
        self.data=data
        self.next=None
class linklist:
    def  __init__(self):
        self.head=None

    def addatbeg(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def print(self):
        current=self.head
        while(current):
            print(current.data,end="-->")
            current=current.next
    def addend(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            return
        currentnode=self.head
        while(currentnode.next):
            currentnode=currentnode.next
        currentnode.next=newnode

    def insertAtIndex(self, data, index):
        if (index == 0):
          self.insertAtBegin(data)

        position = 0
        current_node = self.head
        while (current_node != None and position+1 != index):
           position = position+1
           current_node = current_node.next

        if current_node != None:
          new_node = node(data)
          new_node.next = current_node.next
          current_node.next = new_node
        else:
          print("Index not present")

    def removefirst(self):
        if self.head is None:
            return
        self.head=self.head.next
    def removelast(self):
        if self.head is None:
            return
        current=self.head
        while(current!=None and current.next.next!=None):
            current=current.next
        current.next=None
