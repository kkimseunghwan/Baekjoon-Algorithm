

numbers = [ 30, 120, 10, 90, 80, 20 ]
print("기존 배열 :",numbers)

print("\n=======================================\n")

def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [ number for number in array[1:] if number <= pivot ]
        greater = [ number for number in array[1:] if number >= pivot ]
        return quickSort(less) + [pivot] + quickSort(greater)

result = quickSort(numbers)
print("정렬 후 :",result)













