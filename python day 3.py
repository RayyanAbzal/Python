'''
for i in range(1000):
    print(i)

for i in range(10):
    for j in range(10):
        print("i:"str(i)+)

numbers = [5,4,3,2,1]
length = len(numbers)

for i in range(length):
    for j in range(0, length-i-1):
        if numbers[j] > numbers[j+1] :
            numbers[j], numbers [j+1] = numbers[j+1], numbers [j]
print(numbers)

numbers = [5,4,3,2,1]
length = len(numbers)

# Go through all array elements
for i in range(length):

    # Find the minimum element in remaining
    # unsorted array
    minimum = i
    for j in range(i+1, length):
        if numbers[minimum] > numbers[j]:
            minimum = j
    
    # Swap the found minimum element with
    # the first element
    numbers[i], numbers[minimum] = numbers[minimum], numbers[i]

print(numbers)
'''
import time

start_time = time.time()

for i in range(50000):
    print(i)

end_time = time.time()

print(end_time - start_time)