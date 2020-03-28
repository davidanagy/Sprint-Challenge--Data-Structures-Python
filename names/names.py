import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# --> The runtime of the original code here was O(n^2) <--
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# The below imports assume that the given folders contain the requisite
# data structures.
# import sys
# sys.path.append('../../Data-Structures/binary_search_tree')
# sys.path.append('../../Data-Structures/queue_and_stack')
# sys.path.append('../../Data-Structures/doubly_linked_list')
# from binary_search_tree import BinarySearchTree

# # This has a runtime complexity of O(n log n), I think.
# # It took about 0.1 seconds to run on my computer.
# tree = BinarySearchTree(names_1[0])
# for name_1 in names_1[1:]:
#     tree.insert(name_1)
# for name_2 in names_2:
#     # The "contains" method checks if the value exists in the tree.
#     # On average, its runtime is O(log n).
#     if tree.contains(name_2):
#         duplicates.append(name_2)

# STRETCH SOLUTION
# Basically I want to search names_1 for each name_2, and add to
# "duplicates" if I find it.
# The most efficient search with arrays is a Binary Search,
# so I'll import my code for that.
import sys
sys.path.append('../../Sorting/src/searching')
from searching import binary_search
# To do a binary search, you first have to sort the search array.
names_1.sort()
for name_2 in names_2:
    # binary_search returns a -1 when the item isn't found,
    # so append to duplicates whenever the result isn't -1.
    if binary_search(names_1, name_2) != -1:
        duplicates.append(name_2)

# The runtime for this ended up being about 0.8 seconds on my computer--
# better than the Binary Search Tree!

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
