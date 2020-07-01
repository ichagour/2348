def selection_sort_descend_trace(A):
    for i in range(len(A)-1):
        ind = i
        for j in range(i + 1, len(A)):
            if A[ind] < A[j]:
                ind = j
        A[i], A[ind] = A[ind], A[i]
        for x in A:
            print(x,end=" ")
        print()
    return A

if __name__ == "__main__":
    numbers = [int(x) for x in input("").split()]
    selection_sort_descend_trace(numbers)