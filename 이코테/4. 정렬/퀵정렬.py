
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    
    
even = []
for x in range(10):
    if x % 2 == 0:
        even.append(x)
        

even2 = [x for x in range(10) if x % 2 == 0]

print(even)
print(even2)