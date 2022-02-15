def solution(price, money, count):
        # fee = sum(i*price for i in range(1, count+1))
        # if (fee>money):
        #     return fee-money
        # else:
        #     return 0
        return abs(min(money - sum(i*price for i in range(1, count+1)), 0))