# ---------------------------------------
# Sort algorithm
# ---------------------------------------
import numpy as np

threshold = 2


def quick_sort(A):
    def partition(A, low, hi):
        pivotIndex = get_pivot(A, low, hi)
        pivotValue = A[pivotIndex]
        A[pivotIndex], A[low] = A[low], A[pivotIndex]
        border = low

        for i in range(low, hi + 1):
            if A[i] < pivotValue:
                border += 1
                A[i], A[border] = A[border], A[i]
        A[low], A[border] = A[border], A[low]

        return border

    def get_pivot(A, low, hi):
        mid = (hi + low) // 2
        s = sorted([A[low], A[mid], A[hi]])
        if s[1] == A[low]:
            return low
        elif s[1] == A[mid]:
            return mid
        return hi

    def quick_sort2(A, low, hi):
        if hi - low < threshold and low < hi:
            def q_selection_sort(x, first, last):
                for i in range(first, last):
                    minIndex = i
                    for j in range(i + 1, last + 1):
                        if x[j] < x[minIndex]:
                            minIndex = j
                    if minIndex != i:
                        x[i], x[minIndex] = x[minIndex], x[i]
            q_selection_sort(A, low, hi)  # 在数据量小于阈值的情况下调用选择排序。
        elif low < hi:
            p = partition(A, low, hi)
            quick_sort2(A, low, p - 1)
            quick_sort2(A, p + 1, hi)

    quick_sort2(A, 0, len(A) - 1)


def selection_sort(x):
    first, last = 0, len(x) - 1
    for i in range(first, last):
        minIndex = i
        for j in range(i + 1, last + 1):
            if x[j] < x[minIndex]:
                minIndex = j
        if minIndex != i:
            x[i], x[minIndex] = x[minIndex], x[i]


def insert_sort(A):
    for i in range(1, len(A)):
        j = i - 1
        while A[j] > A[j + 1] and j >= 0:
            A[j], A[j + 1] = A[j + 1], A[j]
            j -= 1


def bubble_sort(A):
    len_A = len(A)
    for i in range(len_A - 1):
        swapped = False
        for j in range(0, len_A - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swapped = True
        if not swapped:
            return


def merge_sort(A):
    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)

        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = arr[l + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

        # Merge the temp arrays back into arr[l..r]
        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = l  # Initial index of merged subarray
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

            # Copy the remaining elements of L[], if there
            # are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

            # Copy the remaining elements of R[], if there
            # are any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def merge_sort2(A, first, last):
        if first < last:
            middle = (first + last) // 2
            merge_sort2(A, first, middle)
            merge_sort2(A, middle + 1, last)
            merge(A, first, middle, last)

    merge_sort2(A, 0, len(A)-1)


np.random.seed(1)
to_sort = [1, -2, 7, 8, 6]
#to_sort = [5, 9, 1, 2, 4, 8, 6, 3, 7, 0, -1, -2, 10, 11, 12, 23, 13, 17, 16]
to_sort = list(range(-100, 100))
np.random.shuffle(to_sort)
print(to_sort)
quick_sort(to_sort)
# insert_sort(to_sort)
# selection_sort(to_sort)
# bubble_sort(to_sort)
# merge_sort(to_sort)
# to_sort.sort()
print(to_sort)
