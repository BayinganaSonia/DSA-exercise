array = [64, 34, 25, 12, 22, 11, 90,5]
n = len(array)

for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            swapped = True
        if not swapped:
            break

print("Sorted array is:", array)
