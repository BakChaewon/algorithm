# 코테 문제에서 살펴본 갖가지 규칙들

1. 키패드의 각 칸 사이 거리는 두 칸의 행 뺄셈과 열 뺄셈 값을 더하고 절댓값을 씌워주면 된다. distance = |(a_row - b_row) + (a_col - b_col)|
   관련 문제 - https://programmers.co.kr/learn/courses/30/lessons/67256

2. 약수 관련 규칙들
   1) 약수 개수는 해당 숫자가 제곱수이면 홀수개이고, 제곱수가 아니라면 짝수개이다.
   2) 어떤 수 n의 n을 제외한 약수는 모두 n//2보다 작거나 같다.
   관련 문제 - https://programmers.co.kr/learn/courses/30/lessons/77884

3. 소수 관련 규칙들
   1) 1보다 큰 모든 자연수는 소수의 곱으로 이루어져있다. 
   2) 어떤 자연수 n이 있을 때, √n 보다 작거나 같은 모든 자연수로 나누어 떨어지지 않으면 n은 소수이다.
   3) 어떤 자연수 n이 있을 때, √n 보다 작은 모든 소수들로 나누어 떨어지지 않으면 n은 소수이다. (3-1과 3-2를 합쳐보면 나오는 결론)
   4) 소수 찾기에 효율적인 방법 -> 에라토스테네스의 체
   관련 문제 - https://programmers.co.kr/learn/courses/30/lessons/12977 , https://programmers.co.kr/learn/courses/30/lessons/12921
