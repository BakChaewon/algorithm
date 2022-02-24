def solution(str1, str2):
    inter = []
    arr_str1 = [str1[i:i+2].lower()for i in range(len(str1)-1) if((str1[i:i+2]).isalpha())]
    arr_str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if((str2[i:i+2]).isalpha())]
    union = arr_str1 + arr_str2 #합집합
    for i in arr_str1:
        if(i in arr_str2):
            inter.append(i)
            arr_str2.remove(i)
    for i in inter:
        union.remove(i)
    if(len(union)==0 and len(inter)==0):
        return 65536
    elif(len(union)==0):
        return 0
    else:
        return int(len(inter)/len(union)*65536)