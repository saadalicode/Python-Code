#  --------Question no 1-------
# implementing stack using List 
my_list = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
my_stack=[]
print(my_list)

print("-----Adding values in Stack-----\n")
# adding elements in the stack 
for i in range(len(my_list)):
    my_stack.append(my_list[i])
    print(my_stack)

print("----Removing values from stack----\n")    
#  removing elements from the stack 
for i in range(len(my_stack)):
    my_stack.pop()
    print(my_stack)

# updating elements in a stack 
my_stack = [1,2,3,4,5,6,7,8,9,20]
def update(location,value):
    if location < len(my_stack):
        my_stack[location]=value
    else:
        print(f"Index {location} is out of range for the stack!!!")

update(5,50)
print(my_stack)

# implement Stacks in python using Arrays
import array as myarray
my_stack = myarray.array('i',[1,2,3,4,5,6,7,8,9,10])

# reading the Stack elements 
for i in my_stack:
    print(i,end=' ')
print("\n")
# inserting elements in the Stack 
my_stack.append(11)
for i in my_stack:
    print(i,end=' ')
print("\n")
# deleting element from the Stack 
for i in range(len(my_stack)):
    my_stack.pop()
    for j in range(len(my_stack)):
        print(j,end=' ')
    print("\n")
# updating elements in a Stack implementd ysing array
stack = myarray.array('i',[1,2,3,4,5])
def update(data, value):
    ind = stack.index(data)
    stack[ind]=value
    for i in stack:
        print(i,end=" ")
update(5,30)

# implement Stacks in Python using deque form the in-bulit collections package 
from collections import deque

my_stack =deque()
my_list = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

# inserting elements in the Stack using deque
for i in my_list:
    my_stack.append(i)
    print(my_stack)
print("\n")
# deleting the elements from the stack using deque
for i in range(len(my_stack)):
    my_stack.pop()
    print(my_stack)
# updating the elements in Stack using deque 
stack =  deque([1,2,3,4,5])
def update(data, value):
    ind = stack.index(data)
    stack[ind]=value
    return stack
update(4,44)
print(stack)

# Sorting the Stack implement using deque 
stack_deq = deque([5,3,1,16,22,33,12,10,2,15])
stack_arr = myarray.array('i',[6,10,2,8,4])
stack_lis = [11,1,15,9,3,7]

# Sorting the Stack implement using deque 
sample = []
def sort_deq():
    for i in range(len(stack_deq)):
        x = stack_deq.pop()
        sample.append(x)
    sample.sort()
    for i in sample:
        stack_deq.append(i)
    return stack_deq

sort_deq()
print("----After sorting Stack deque elements----\n")
print(stack_deq)

#  Sorting Stack implementd using arrays
sample=[]
def sort_arr():
    while stack_arr:
        x = stack_arr.pop()
        sample.append(x)
    sample.sort()
    for i in sample:
        stack_arr.append(i)
    
    return stack_arr
sort_arr()
print("----After sorting Stack Array elements----\n")
print(stack_arr)

def sort_list():
    stack_lis.sort()
    return stack_lis

sort_list()
print("----After sorting Stack List elements----\n")
print(stack_lis)

# -------Question no 2--------
# implement Queues using Lists
my_list = ['assembly','java', 'python', 'css','dart']
my_queue = []
print(my_list)

# adding elements in the queue 
for i in range(len(my_list)):
    my_queue.append(my_list[i])
    print(my_queue)

# deleting element from the queue 
for i in range(len(my_queue)):
    my_queue.pop(0)
    print(my_queue)

# updating queue implemented using the lists 
my_queue = [1,2,3,4,5,6,7]
def update(data, value):
    for i in range(len(my_queue)):
        if my_queue[i]==data:
            my_queue[i]=value
    return my_queue

update(3,33)
print("----After Updating Queue List elements----\n")
print(my_queue)

#  implement Queue using Arrays 
my_queue  = myarray.array('i',[1,2,3,4,5])

# reading the queue 
for i in my_queue:
    print(i, end=" ")
print("\n")
# inserting elemnts in the queue
my_queue.append(6) 
for i in my_queue:
    print(i, end=" ")
print("\n")
#deleting elements from the queue
for i in range(len(my_queue)):
    my_queue.pop(0)
    for i in my_queue:
        print(i, end=" ")
    print("\n")

# updating elements in a queue implemented using Arrays
queue = myarray.array('i',[1,2,3,4,5])
def update(data,value):
    ind = queue.index(data)
    queue[ind]=value
    for i in queue:
        print(i,end=" ")
    
update(2,22)
print("----After Updating Queue Array elements----\n")
print(queue)

# implemented queue Using Deque 
my_list = ['assembly','java', 'python', 'css','dart']
my_queue = deque()

# inserting elements using append()
for i in my_list:
    my_queue.append(i)
    print(my_queue)
print("\n")
# deleting elements using popleft()
for i in range(len(my_queue)):
    my_queue.popleft()
    print(my_queue)
print("\n")
# adding elements using appendleft()
for i in my_list:
    my_queue.appendleft(i)
    print(my_queue)
print("\n")
# removing elements using pop() 
for i in range(len(my_queue)):
    my_queue.pop()
    print(my_queue)
print("\n")

# updating the elements in queue implemented using deque 
my_queue = deque([1,2,3,4,5])
def update(data,value):
    ind = my_queue.index(data)
    my_queue[ind]=value
    return my_queue
update(4,40)
print("----After updating Queue element using deque----\n")
print(my_queue)

# Sorting a Queue 
queue_deq = deque([5,3,12,33,22,25,7,2])
queue_arr = myarray.array('i',[20,4,11,2,33,55])
queue_lis = [21,2,11,44,33,9]

sample=[]
def sortDeq():
    for i in range(len(queue_deq)):
        res =queue_deq.popleft()
        sample.append(res)
    
    sample.sort()

    for i in sample:
        queue_deq.append(i)

    return queue_deq

sortDeq()
print("----After Sorting Queue using Deque----\n")
print(queue_deq)

sample=[]
def sortArr():
    for i in range(len(queue_arr)):
        res =queue_arr.pop()
        sample.append(res)
    
    sample.sort()

    for i in sample:
        queue_arr.append(i)

    return queue_arr

sortArr()
print("----After Sorting Queue using Array----\n")
print(queue_arr)

def sortList():
    queue_lis.sort()
    return queue_lis

sortList()
print("----After Sorting Queue using List----\n")
print(queue_lis)

# Question no 3 
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # If target is not present in array
    return -1

# Example usage:
sorted_array = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target_value = 12
result_index = binary_search(sorted_array, target_value)

if result_index != -1:
    print(f"Target {target_value} found at index {result_index}.")
else:
    print(f"Target {target_value} not found in the array.")
