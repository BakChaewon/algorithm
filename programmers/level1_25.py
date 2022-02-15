def binary(arr, n):
    tmp = []
    for i in arr:
        tmp.append(list(bin(i)))
    for j in tmp:
        if(len(j)<n):
            while(len(j)!=n):
                j.insert(0, 0) #insert와 append의 차이
    return tmp

def solution(n, arr1, arr2):
    arr1 = binary(arr1, n)
    arr2 = binary(arr2, n)
    tmp = [[i+j for i,j in zip(A,B)] for A,B in zip(arr1,arr2)]
    tmp=[[" " if i==0 else "#" for i in A]for A in tmp]
    return ["".join(A) for A in tmp]