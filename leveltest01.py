def solution(arr1, arr2):
    arr_list = []
    answer = []
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr_list.append(arr1[i][j] + arr2[i][j])
            print(arr_list)
        answer.append(arr_list)
        arr_list = []

    return answer


arr1 = [[1],[2]]
arr2 = [[3],[4]]
print(solution(arr1, arr2))