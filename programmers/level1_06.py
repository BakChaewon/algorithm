def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        for r in range(len(board)):
            if(board[r][i-1]!=0):
                basket.append(board[r][i-1])
                board[r][i-1] = 0

                if(len(basket)<2):
                    break
                if(basket[-1]==basket[-2]):
                    del basket[-2:]
                    answer+=2
                break
                    
    return answer