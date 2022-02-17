def solution(numbers, hand):
    answer = ''
    left = '*'
    right = '#'

    dic = {1:(0,0), 2:(0,1), 3:(0,2),
          4:(1,0), 5:(1,1), 6:(1,2),
          7:(2,0), 8:(2,1), 9:(2,2),
          '*':(3,0), 0:(3,1), '#':(3,2)}
    
    for i in numbers:
        if(i==1 or i==4 or i==7):
            answer+='L'
            left=i
        elif(i==3 or i==6 or i==9):
            answer+='R'
            right=i
        else:
            dis_right = abs(dic[i][0]-dic[right][0])+abs(dic[i][1]-dic[right][1])
            dis_left = abs(dic[i][0]-dic[left][0])+abs(dic[i][1]-dic[left][1])
            
            if(dis_right<dis_left):
                right=i
                answer+='R'
            elif (dis_right>dis_left):
                left=i
                answer+='L'
            else:
                if(hand=="left"):
                    left=i
                    answer+='L'
                else:
                    right=i
                    answer+='R'         
    return answer