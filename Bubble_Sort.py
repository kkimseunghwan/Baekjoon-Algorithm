
# 버블정렬 : 거품이 물에서 떠오르는 모양
# 핵심로직 : 첫번째, 두번째랑 비교하여 두번째가 더 작을시 첫번째랑 자리를 바꿈

numbers = [ 7, 3, 2, 9 ,4 ] 

print("기존 배열 :",numbers)

print("\n=======================================\n")

# for문 적용, 함수로 만들기
def bubble(arr):
    for front_index in range( 0, len(arr)-1 ):
        for index in range( front_index+1, len(arr) ): # 1,2,3
            if arr[front_index] > arr[index]: # 비교 후
                #자리를 바꿔준다
                temp = arr[front_index]
                arr[front_index] = arr[index]
                arr[index] = temp
    return arr

result = bubble(numbers)
print("정렬 후 :",result)







