1. str
    - .upper(), .lower() 함수를 통해 문자의 대소문자 변경 가능
    - f-string - format과 유사하게 print(f'hello {name}')과 같이 변수를 대괄호 안에 써서 바로 print 가능. 이 함수를 통해 int를 str으로 변환할 수도 있음
    - max() - str에서도 max 함수 사용이 가능. 유니코드 값이 큰 인자 반환. 숫자로 이루어진 문자열이 들어온다면 가장 앞의 숫자로 비교. 2000 vs 899면 899반환
    - string.startwith(tmp), endwith - tmp 문장으로 시작하냐, 끝나냐 를 확인할 수 있는 함수
    - [::-1]을 사용해 문자열 혹은 리스트를 뒤집을 수 있음
2. list
    - prod(list)는 각 원소의 곱을 반환. 리스트가 행렬일 경우 각 열의 곱을 반환한다. → numpy 함수
    - join() - "".join(list) 와 같이 리스트 내 요소를 한 문장으로 결합할 수 있음
    - swap - arr[1], arr[2] = arr[2], arr[1] 과 같이 한줄로 swap 가능
3. int
    - not() 함수를 통해 0을 True로 0이 아닌 값을 False로 만들 수 있음. not(0)==True / not(22)==False
4. 연산자
    - ^ : XOR 연산자로 두 값이 같으면 0을 반환, 다르면 1을 반환 → tmp ^= 1과 같이 사용 가능
    - or : 문자열 간 or 연산도 가능
5. 집합
    - set() : 중복된 숫자가 몇개인지 확인하기 위해 set 함수를 사용할 수도 있음
6. dict
    - `dict(zip(['w','s','d','a'], [1,-1,10,-10]))` 와 같이 dictionary를 만들 수 있다..
