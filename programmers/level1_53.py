def solution(arr1, arr2):
    return [[i+j for i,j in zip(A, B)] for A, B in zip(arr1,arr2)]