#Note: to create an empty set you have to use set(), not {};

set= {1,2,4,5,5,5,5,66,678,3,3}
print(set)

#each time show the different results
set2= {1,2,3,4,44,5,4,4,"a","a","b",1.25}
print(set2)

# my_set = {[123, 452, 5, 6]} # TypeError: unhashable type: 'list'
# print(my_set)

set2.add(142)
print(set2)

set2.remove(142)
print(set2)

set2.discard(145) #No error if not found 
print(set2)
print(len(set2))

my_set = {1, 2, 3, 4}
print(3 in my_set)  # True

# O(1)
# Python uses a hash function to calculate the position (index) in memory where the value should be
# — so it can go directly to it, like jumping to a room by number.